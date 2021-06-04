from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=130)
    file = models.FileField(upload_to='notices/')
    added_on = models.DateTimeField(
        auto_now_add=True, blank=True)


class Result(models.Model):
    title = models.CharField(max_length=130)
    file = models.FileField(upload_to='results/')
    added_on = models.DateTimeField(
        auto_now_add=True, blank=True)
