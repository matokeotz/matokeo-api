from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

from api.models.school_models import School

# model for regions
class Region(Model):
    '''
        Stores information on a single region
    '''

    name = CharField(max_length=50, unique=True, null=False, default="Unknown Region", db_index=True)
    latitude = DecimalField(max_digits=13, decimal_places=10, default= -6.3690 )
    longitude = DecimalField(max_digits=13, decimal_places=10, default= 34.8888)

    def __str__(self):
        return self.name

# model for districts
class District(Model):
    '''
        Stores information on a single district
    '''

    name = CharField(max_length=50, unique=True, null=False, default="Unknown District")
    latitude = DecimalField(max_digits=13, decimal_places=10, default=-6.3690)
    longitude = DecimalField(max_digits=13, decimal_places=10, default= 34.8888)

    def __str__(self):
        return self.name

# model for zones
class Zone(Model):
    '''
        Stores information on a single zone
    '''

    name = CharField(max_length=50, unique=True, null=False, default="Unknown Zone")

    def __str__(self):
        return self.name

# model to link schools with zones and regions
class SchoolLocation(Model):
    '''
        Stores information on the region, district,
        and zone that a specific school is located
        in. Relates :model:`api.School`,
        :model:`api.Region`, :model:`api.District`,
        and :model:`api.Zone`.
    '''

    school = ForeignKey(School)
    region = ForeignKey(Region)
    district = ForeignKey(District)
    zone = ForeignKey(Zone)
    latitude = DecimalField(max_digits=13, decimal_places=10, default=-6.3690)
    longitude = DecimalField(max_digits=13, decimal_places=10, default=34.8888)

    def __str__(self):
        return self.school