from django.shortcuts import render
from django.views.generic import ListView
from .models import Notice
from django.contrib.auth.mixins import LoginRequiredMixin


class AllNotices(LoginRequiredMixin, ListView):
    template_name = "notice/all_notes.html"
    queryset = Notice.objects.all()
    context_object_name = "notices"
