from django.views.generic import CreateView, UpdateView, DetailView
from authy.models import Student, User
from authy.forms import StudentSignUpForm, StudentUpdateForm
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "authy/student_update.html"
    form_class = StudentUpdateForm

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("/")


class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = "authy/student_detail.html"
    context_object_name = "student"
    queryset = Student.objects.all()
