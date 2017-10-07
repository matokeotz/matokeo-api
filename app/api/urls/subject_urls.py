from django.conf.urls import url

from api.views.subject_views import SubjectView

urlpatterns = [
    url(r'^subjects/', SubjectView.as_view(), name = 'subjects'),
]