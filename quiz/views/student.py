from django.views.generic import CreateView, ListView, UpdateView
from django.db.models import Count
from authy.decorators import student_required
from authy.mixins import StudentLoginMixin
from authy.models import Quiz, TakenQuiz
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView

from ..forms import TakeQuizForm
from authy.models import Quiz, TakenQuiz


class QuizListView(StudentLoginMixin, ListView):
    model = Quiz
    ordering = ('name', )
    context_object_name = 'quizzes'
    template_name = 'quiz/student/quiz_list.html'
    paginate_by = 10

    def get_queryset(self):
        student = self.request.user.student
        student_degree_batch = student.degree_batch
        taken_quizzes = student.quizzes.values_list('pk', flat=True)
        queryset = Quiz.objects.filter(subject=student_degree_batch) \
            .exclude(pk__in=taken_quizzes) \
            .annotate(questions_count=Count('questions')) \
            .filter(questions_count__gt=0)
        return queryset


@login_required
@student_required
def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    student = request.user.student

    if student.quizzes.filter(pk=pk).exists():
        return render(request, 'students/taken_quiz.html')

    total_questions = quiz.questions.count()
    unanswered_questions = student.get_unanswered_questions(quiz)
    total_unanswered_questions = unanswered_questions.count()
    progress = 100 - \
        round(((total_unanswered_questions - 1) / total_questions) * 100)
    question = unanswered_questions.first()

    if request.method == 'POST':
        form = TakeQuizForm(question=question, data=request.POST)
        if form.is_valid():
            with transaction.atomic():
                student_answer = form.save(commit=False)
                student_answer.student = student
                student_answer.save()
                if student.get_unanswered_questions(quiz).exists():
                    return redirect('students:take_quiz', pk)
                else:
                    correct_answers = student.quiz_answers.filter(
                        answer__question__quiz=quiz, answer__is_correct=True).count()
                    score = round(
                        (correct_answers / total_questions) * 100.0, 2)
                    TakenQuiz.objects.create(
                        student=student, quiz=quiz, score=score)
                    return redirect('students:quiz_list')
    else:
        form = TakeQuizForm(question=question)

    return render(request, 'quiz/student/take_quiz_form.html', {
        'quiz': quiz,
        'question': question,
        'form': form,
        'progress': progress
    })


class TakenQuizListView(StudentLoginMixin, ListView):
    model = TakenQuiz
    context_object_name = 'taken_quizzes'
    ordering = ('-date')
    template_name = 'quiz/student/taken_quiz_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = self.request.user.student.taken_quizzes \
            .select_related('quiz', 'quiz__subject') \
            .order_by('quiz__name')
        return queryset
