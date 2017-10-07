from django.conf.urls import url

from api.views.student_views import StudentView

urlpatterns = [
    url(r'^students/', StudentView.as_view(), name = 'students'),

]