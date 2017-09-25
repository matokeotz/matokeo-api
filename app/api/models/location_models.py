from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

from api.models.school_models import School
# model for regions
class Region(Model):
    name = CharField(max_length=50, unique=True, null=False, default="Unknown Region", db_index=True)
    latitude = DecimalField(max_digits=13, decimal_places=10, default= -6.3690 )
    longitude = DecimalField(max_digits=13, decimal_places=10, default= 34.8888)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/region/'+ self.name.lower() + '/'

# model for districts
class District(Model):
    name = CharField(max_length=50, unique=True, null=False, default="Unknown District")
    latitude = DecimalField(max_digits=13, decimal_places=10, default=-6.3690)
    longitude = DecimalField(max_digits=13, decimal_places=10, default= 34.8888)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/region/district/'+ self.name.lower() + '/'

# model for zones
class Zone(Model):
    name = CharField(max_length=50, unique=True, null=False, default="Unknown Zone")

    def __str__(self):
        return self.name

# model to link schools with zones and regions
class SchoolLocation(Model):
    zone = ForeignKey(Zone)
    school = ForeignKey(School)
    region = ForeignKey(Region)
    district = ForeignKey(District)
    latitude = DecimalField(max_digits=13, decimal_places=10, default=-6.3690 )
    longitude = DecimalField(max_digits=13, decimal_places=10, default=34.8888)

    def __str__(self):
        return self.school