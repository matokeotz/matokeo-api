from django.conf.urls import url

from api.views.subject_views import SubjectView, SubjectGradeStatisticsView

urlpatterns = [
    url(r'^subjects/', SubjectView.as_view(), name='subjects'),
    url(r'^schools/(?P<school>[a-zA-Z-]+)/statistics', SubjectGradeStatisticsView.as_view(), name='subjectgradestatistics'),
]