from django.views.generic import ListView
from .models import Notice, Result
from django.contrib.auth.mixins import LoginRequiredMixin


class ListNotices(LoginRequiredMixin, ListView):
    template_name = "notice/all_notes.html"
    queryset = Notice.objects.order_by('-added_on')
    context_object_name = "notices"
    paginate_by = 15


class ListResults(LoginRequiredMixin, ListView):
    template_name = "notice/all_results.html"
    queryset = Result.objects.order_by('-added_on')
    context_object_name = "results"
    paginate_by = 15
