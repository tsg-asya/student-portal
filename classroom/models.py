from django.db import models
import uuid
from authy.models import User, Degree_Batch

# 3rd apps field
from ckeditor.fields import RichTextField


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    degree_batch = models.ForeignKey(Degree_Batch, on_delete=models.CASCADE)
    syllabus = RichTextField()
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='course_owner')
    enrolled = models.ManyToManyField(User)
