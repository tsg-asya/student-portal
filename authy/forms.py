from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.utils.text import slugify
from django.forms.utils import ValidationError
from authy.models import User, Student, Degree_Batch

# custom validators


def ForbiddenUsers(value):
    forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root',
                       'email', 'user', 'join', 'sql', 'static', 'python', 'delete']
    if value.lower() in forbidden_users:
        raise ValidationError(
            'Invalid name for user, this is a reserverd word.')


def InvalidUser(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError(
            'This is an Invalid user, Do not user these chars: @ , - , + ')


def UniqueEmail(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this email already exists.')


def UniqueUser(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this username already exists.')


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(
        max_length=30, required=True, label='College Email')
    degree_batch = forms.ModelChoiceField(
        queryset=Degree_Batch.objects.all(), required=True, empty_label=None)

    class Meta(UserCreationForm.Meta):
        model = User

    field_order = ['first_name', 'last_name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsers)
        self.fields['username'].validators.append(InvalidUser)
        self.fields['username'].validators.append(UniqueUser)
        self.fields['email'].validators.append(UniqueEmail)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.save()
        student = Student.objects.create(
            user=user,
            slug=slugify(user.username),
            degree_batch=self.cleaned_data['degree_batch']
        )
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


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'enrollment_no',
            'contact',
            'local_address',
            'city_state',
            'guardian_name',
            'guardian_contact_no',
            'birthdate',
            'picture'
        )

        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['enrollment_no'].label = "Enrollment Number"
        self.fields['contact'].label = "Personal Number"
        self.fields['guardian_name'].label = "Guardian's Full Name"
        self.fields['birthdate'].label = "Date of Birth"
        self.fields['local_address'].label = "Address"
        self.fields['city_state'].label = "City/State"
        self.fields['guardian_contact_no'].label = "Guardian's Contact Number"
