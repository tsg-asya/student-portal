from django import forms
from ckeditor.widgets import CKEditorWidget
from authy.models import Degree_Batch

from .models import Course


class NewCourseForm(forms.ModelForm):
    title = forms.CharField(required=True, label='Course Title')
    description = forms.CharField(
        required=True, widget=forms.Textarea(attrs={'cols': 80, 'rows': 3}), label='Short Description')
    degree_batch = forms.ModelChoiceField(
        queryset=Degree_Batch.objects.all(), empty_label=None, label='Degree/Batch')
    syllabus = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Course
        fields = ('title', 'description', 'degree_batch', 'syllabus')
