from django.urls import path, include
from quiz.views import student, teacher

urlpatterns = [
    path('students/', include(([
        path('', student.QuizListView.as_view(), name='quiz_list'),
        path('taken/', student.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', student.take_quiz, name='take_quiz'),
    ], 'quiz'), namespace='students')),

    path('teachers/', include(([
        path('', teacher.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', teacher.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teacher.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/',
             teacher.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/',
             teacher.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/',
             teacher.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/',
             teacher.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/',
             teacher.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'quiz'), namespace='teachers')),

]
