from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authy.views import signup, student, teacher
from django.contrib.auth.views import LoginView
from classroom.views import LandingPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authy.urls')),
    path('', LandingPage.as_view(), name='index'),
    path('accounts/login/',
         LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/',
         student.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/',
         teacher.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('classroom/', include('classroom.urls')),
    path('notices/', include('notice.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
