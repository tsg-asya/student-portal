from django.urls import path
from . import views

urlpatterns = [
    path('catalog/<slug:degree_slug>', views.Catalog, name='course_catalog'),
    path('course/create', views.CourseCreateView.as_view(), name='course_create'),
    path('course/id/<course_id>', views.CourseDetail, name='course_detail'),
    path('course/<course_id>/update',
         views.UpdateCourse, name='course_update'),
    path('course/<course_id>/delete',
         views.DeleteCourse, name='course_delete')
]
