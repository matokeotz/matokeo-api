from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from django_filters.rest_framework import Filter, FilterSet
from django_filters.fields import Lookup

from api.utils.filters import field_filter

from api.models.student_models import Student, StudentSubjectGrade

from api.serializers.student_serializers import StudentSerializer, StudentSubjectGradeSerializer, SchoolStudentSerializer

class StudentView(ListAPIView):
    ''' 
        This is a read-only views represents
        `Student`.

        get:
        Return a list of all available students

    '''

    model = Student
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentSubjectGradeFilter(FilterSet):
    subject = Filter(name='subject__name', method=field_filter)
    grade = Filter(name='grade__letter', method=field_filter)

    class Meta:
        model = StudentSubjectGrade
        fields = ('student', 'subject', 'grade')

class StudentSubjectGradeView(ListAPIView):
    '''
        This is a read-only view that represents
        `StudentSubjectGrade`. 

        get:
        Returns a list of grades by subject for
        a given student. Provides filters for
        `subject` and `grade`.
    '''

    serializer_class = StudentSubjectGradeSerializer
    filter_class = StudentSubjectGradeFilter
    
    def get_queryset(self):
        student = self.kwargs['student']
        return StudentSubjectGrade.objects.filter(student__identifier=student)

class SchoolStudentFilter(FilterSet):
    graduation_year = Filter(name='graduation_year', method=field_filter)
    gender = Filter(name='gender', method=field_filter)
    division = Filter(name='division', method=field_filter)
    aggregate_score = Filter(name='aggregate_score', method=field_filter)

    class Meta:
        model = Student
        fields = ('graduation_year', 'gender', 'division', 'aggregate_score')

class SchoolStudentView(ListAPIView):
    '''
        This is a read-only view that represents
        `SchoolStudent`.

        get:
        Returns a list of students by a given
        school. Provides filters for `graduation_year`,
        `gender`, `division`, and `aggregate_score`.
    '''

    serializer_class = SchoolStudentSerializer
    filter_class = SchoolStudentFilter

    def get_queryset(self):
        school = self.kwargs['school']
        return Student.objects.filter(school__short_name=school)