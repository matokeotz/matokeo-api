from django.conf.urls import url

from api.views.student_views import StudentView, StudentSubjectGradeView, SchoolStudentView

urlpatterns = [
    url(r'^student/(?P<student>[a-zA-Z-0-9]+)/', StudentSubjectGradeView.as_view(), name='studentsubjectgrade'),
    url(r'^students/', StudentView.as_view(), name='students'),
    url(r'^schools/(?P<school>[a-zA-Z-0-9]+)/students/', SchoolStudentView.as_view(), name='schoolstudent'),

]