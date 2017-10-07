from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from django_filters.rest_framework import Filter, FilterSet
from django_filters.fields import Lookup

from api.models.student_models import Student

from api.serializers.student_serializers import StudentSerializer

class StudentView(ListAPIView):
    ''' 
        This is a read-only views that lets users
        see a list of all available schools
    '''
    model = Student
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
