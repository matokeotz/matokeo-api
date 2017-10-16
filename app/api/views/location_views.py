from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from django_filters.rest_framework import Filter, FilterSet
from django_filters.fields import Lookup

from api.utils.filters import field_filter

from api.models.location_models import Region, District, Zone, SchoolLocation

from api.serializers.location_serializers import RegionSerializer, DistrictSerializer, ZoneSerializer, SchoolLocationSerializer

class RegionView(ListAPIView):
    '''
        This is a read-only view that represents
        `Region`.

        get:
        Return a list of all available regions.
    '''

    model = Region
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

class DistrictView(ListAPIView):
    '''
        This is a read-only view that represents
        `District`.

        get:
        Return a list of all available districts.
    '''

    model = District
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

class ZoneView(ListAPIView):
    '''
        This is a read-only view that represents
        `Zone`.

        get:
        Return a list of all available zones.
    '''

    model = Zone
    serializer_class = ZoneSerializer
    queryset = Zone.objects.all()

class SchoolLocationFilter(FilterSet):
    district = Filter(name='district', method=field_filter)

    class Meta:
        model = SchoolLocation
        fields = ['district']

class SchoolLocationView(ListAPIView):
    '''
        This is a read-only view that represents
        `SchoolLocation`. 

        get:
        Returns a list of all available schools
        in the given region. Provides filters
        for `district`.
    '''

    serializer_class = SchoolLocationSerializer
    filter_class = SchoolLocationFilter

    def get_queryset(self):
        region = self.kwargs['region']
        return SchoolLocation.objects.filter(region__name=region)