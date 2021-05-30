from django.urls import path
from . import views

urlpatterns = [
    path('tt', views.test, name='tt')
]
