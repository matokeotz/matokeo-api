from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from django_filters.rest_framework import Filter, FilterSet
from django_filters.fields import Lookup

from api.models.location_models import Region, District, Zone, SchoolLocation

from api.serializers.location_serializers import RegionSerializer, DistrictSerializer, ZoneSerializer, SchoolLocationSerializer

class RegionView(ListAPIView):

    model = Region
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

class DistrictView(ListAPIView):

    model = District
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

class ZoneView(ListAPIView):

    model = Zone
    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()

class SchoolLocationView(ListAPIView):

    model = SchoolLocation
    serializer_class = SchoolLocationSerializer
    queryset = SchoolLocation.objects.all()