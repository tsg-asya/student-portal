from django.views.generic import CreateView
from authy.models import User
from authy.forms import TeacherSignUpForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import UserPassesTestMixin


class TeacherSignUpView(UserPassesTestMixin, CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

    def test_func(self):
        return not self.request.user.is_authenticated
