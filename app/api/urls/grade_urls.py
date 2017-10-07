from django.conf.urls import url

from api.views.grade_views import GradeView

urlpatterns = [
    url(r'^grades/', GradeView.as_view(), name = 'grades'),
]