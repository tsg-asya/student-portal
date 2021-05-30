from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class StudentLoginMixin(AccessMixin):
    # Verify the current user is authenticated and a student

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_student:
            return redirect("index")
        return super().dispatch(request, *args, **kwargs)


class TeacherLoginMixin(AccessMixin):
    # Verify the current user is authenticated and a teacher

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_teacher:
            return redirect("index")
        return super().dispatch(request, *args, **kwargs)
