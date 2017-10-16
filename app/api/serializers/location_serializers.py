from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField,\
    SlugRelatedField, HyperlinkedIdentityField
from rest_framework import serializers

from api.models.location_models import Region, District, Zone, SchoolLocation

class RegionSerializer(ModelSerializer):

    class Meta:
        model = Region
        fields = ('name', 'latitude', 'longitude')

class DistrictSerializer(ModelSerializer):

    class Meta:
        model = District
        fields = ('name', 'latitude', 'longitude')

class ZoneSerializer(ModelSerializer):

    class Meta:
        model = Zone
        fields = ('name')

class SchoolLocationSerializer(ModelSerializer):
    school = StringRelatedField()
    region = StringRelatedField()
    district = StringRelatedField()
    zone = StringRelatedField()

    class Meta:
        model = SchoolLocation
        fields = ('school', 'region', 'district', 'zone', 'latitude', 'longitude')
