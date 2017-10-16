from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from django_filters.rest_framework import Filter, FilterSet
from django_filters.fields import Lookup

from api.models.grade_models import Grade

from api.serializers.grade_serializers import GradeSerializer

class GradeView(ListAPIView):
    '''
        This is a read-only view that represents
        `Grade`.

        get:
        Return a list of all available grades
    '''

    model = Grade
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()