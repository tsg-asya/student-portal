from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from authy.models import User, Student


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(
        max_length=30, required=True, label='College Email')

    class Meta(UserCreationForm.Meta):
        model = User

    field_order = ['first_name', 'username', 'email']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data["first_name"]
        user.email = self.cleaned_data["email"]
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user
