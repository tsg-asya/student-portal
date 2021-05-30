from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db.models import fields

from .models import Course, Degree_Batch


class NewCourseForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    degree_batch = forms.ModelChoiceField(queryset=Degree_Batch.objects.all())
    syllabus = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Course
        fields = ('title', 'description', 'degree_batch', 'syllabus')
