from django.views.generic import CreateView
from authy.models import User
from authy.forms import StudentSignUpForm
from django.contrib.auth import login
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
