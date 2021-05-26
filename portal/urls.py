from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authy.views import signup, student, teacher


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/',
         student.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/',
         teacher.TeacherSignUpView.as_view(), name='teacher_signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
