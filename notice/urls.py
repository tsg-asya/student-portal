from django.urls import path
from notice.views import AllNotices

urlpatterns = [
    path('', AllNotices.as_view(), name='all_notices')
]
