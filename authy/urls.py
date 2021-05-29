from django.urls import path
from .views import student

urlpatterns = [
    path('profile/<slug:slug>', student.StudentDetailView.as_view(),
         name='student_detail'),
    path('profile/<slug:slug>/update', student.StudentUpdateView.as_view(),
         name='student_update')
]
