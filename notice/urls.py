from django.urls import path
from notice.views import ListNotices, ListResults

urlpatterns = [
    path('', ListNotices.as_view(), name='all_notices'),
    path('results/', ListResults.as_view(), name='all_results')
]
