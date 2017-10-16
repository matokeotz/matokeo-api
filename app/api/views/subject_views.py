from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from django_filters.rest_framework import Filter, FilterSet
from django_filters.fields import Lookup

from api.utils.filters import field_filter

from api.models.subject_models import Subject, SubjectGradeStatistics

from api.serializers.subject_serializers import SubjectSerializer, SubjectGradeStatisticsSerializer

class SubjectView(ListAPIView):
    '''
        This is a read-only view that represents
        `Subject`.

        get:
        Returns a list of all available subjects
    '''

    model = Subject
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class SubjectGradeStatisticsFilter(FilterSet):
    grade = Filter(name='grade__letter', method=field_filter)
    exam_year = Filter(name='exam_year', method=field_filter)
    subject = Filter(name='subject__name', method=field_filter)
    student_count = Filter(name='student_count', method=field_filter)
    gender = Filter(name='gender', method=field_filter)

    class Meta:
        model = SubjectGradeStatistics
        fields = ('subject', 'grade', 'exam_year', 'gender', 'student_count')

class SubjectGradeStatisticsView(ListAPIView):
    '''
        This is a read-only view that represents
        `SubjectGradeStatistics`.

        get:
        Returns a list of records documenting the
        number of instances of a certain grade for a 
        certain subject in a given year by school.
        Provides filters for `grade`, `exam_year`, `subject`,
        `student_count`, and `gender`.
    '''

    serializer_class = SubjectGradeStatisticsSerializer
    filter_class = SubjectGradeStatisticsFilter

    def get_queryset(self):
        school = self.kwargs['school']
        return SubjectGradeStatistics.objects.filter(school__short_name=school)