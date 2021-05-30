from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def test(request):
    return HttpResponse("<h1>Hello</h1>")


class LandingPage(TemplateView):
    template_name = 'index.html'
