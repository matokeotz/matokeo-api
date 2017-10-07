from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from django_filters.rest_framework import Filter, FilterSet
from django_filters.fields import Lookup

from api.models.subject_models import Subject

from api.serializers.subject_serializers import SubjectSerializer

class SubjectView(ListAPIView):

    model = Subject
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()