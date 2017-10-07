from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from django_filters.rest_framework import Filter, FilterSet
from django_filters.fields import Lookup

from api.models.school_models import School, SchoolStatistics

from api.serializers.school_serializers import SchoolSerializer, SchoolStatisticsSerializer

class SchoolView(ListAPIView):
    ''' 
        This is a read-only view that lets users
        see a list of all available schools
    '''
    model = School
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

class SchoolStatisticsView(ListAPIView):
    '''
        This is a read-only view that lets users
        see a exam years by school
    '''
    model = SchoolStatistics
    serializer_class = SchoolStatisticsSerializer
    queryset = SchoolStatistics.objects.all()