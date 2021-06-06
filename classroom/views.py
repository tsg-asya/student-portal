from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from authy.mixins import TeacherLoginMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Course
from .forms import NewCourseForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from authy.decorators import student_required, teacher_required
from authy.models import Degree_Batch


class LandingPage(TemplateView):
    template_name = 'index.html'


class CourseCreateView(TeacherLoginMixin, CreateView):
    template_name = "classroom/course_create.html"
    form_class = NewCourseForm

    def get_success_url(self):
        return reverse("course_detail", kwargs={'course_id': self.object.id})

    def form_valid(self, form):
        course = form.save(commit=False)
        course.user = self.request.user
        course.save()
        return super().form_valid(form)


@teacher_required
@login_required
def UpdateCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)

    if user != course.user:
        return HttpResponseForbidden()

    else:
        if request.method == 'POST':
            form = NewCourseForm(request.POST, instance=course)
            if form.is_valid():
                course.title = form.cleaned_data.get('title')
                course.description = form.cleaned_data.get('description')
                course.degree_batch = form.cleaned_data.get('degree_batch')
                course.syllabus = form.cleaned_data.get('syllabus')
                course.save()
                return HttpResponseRedirect(reverse("course_detail", kwargs={'course_id': course.id}))
        else:
            form = NewCourseForm(instance=course)

    context = {
        'form': form,
        'course': course
    }

    return render(request, 'classroom/course_update.html', context)


@login_required
def CourseDetail(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    teacher_mode = False
    user_exist_in_course = False
    if user.course_set.filter(pk=course_id).exists():
        user_exist_in_course = True
    if user == course.user:
        teacher_mode = True

    context = {
        'course': course,
        'user_exist_in_course': user_exist_in_course,
        'teacher_mode': teacher_mode,
    }

    return render(request, 'classroom/course.html', context)


@teacher_required
@login_required
def DeleteCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)

    if user != course.user:
        return HttpResponseForbidden()
    else:
        course.delete()
    return redirect('index')


@student_required
@login_required
def Catalog(request, degree_slug):
    degree_batch = get_object_or_404(Degree_Batch, slug=degree_slug)
    courses = Course.objects.filter(
        degree_batch=degree_batch).order_by('-created_at')
    context = {
        'degree_batch': degree_batch,
        'courses': courses
    }
    return render(request, "classroom/course_catalog.html", context)


@student_required
@login_required
def Enroll(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    if user.course_set.filter(pk=course_id).exists():
        # remove if already exists
        course.enrolled.remove(user)
    else:
        course.enrolled.add(user)
    return HttpResponseRedirect(reverse('course_detail', kwargs={'course_id': course_id}))


@login_required
def MyCourses(request):
    user = request.user
    courses = Course.objects.filter(Q(user=user) | Q(enrolled=user)).distinct()
    context = {
        'username': user.username,
        'courses': courses
    }

    return render(request, 'classroom/mycourses.html', context)
