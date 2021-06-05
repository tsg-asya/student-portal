from django.views.generic import CreateView, ListView, UpdateView
from django.db.models import Count
from authy.decorators import student_required, teacher_required
from authy.mixins import StudentLoginMixin, TeacherLoginMixin
from authy.models import Quiz, TakenQuiz


class QuizListView(StudentLoginMixin, ListView):
    model = Quiz
    ordering = ('name', )
    context_object_name = 'quizzes'
    template_name = 'quiz/student/quiz_list.html'

    def get_queryset(self):
        student = self.request.user.student
        student_degree_batch = student.degree_batch
        # taken_quizzes = student.quizzes.values_list('pk', flat=True)
        queryset = Quiz.objects.filter(subject=student_degree_batch) \
            .annotate(questions_count=Count('questions')) \
            .filter(questions_count__gt=0)
        return queryset
