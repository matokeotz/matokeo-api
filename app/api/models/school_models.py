from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

# model to represent schools
class School(Model):
    cno = CharField(max_length=10, null=False)
    short_name = CharField(max_length=50, null=False, unique=True, db_index=True)
    long_name = CharField(max_length=100, null=False)
    gender = CharField(max_length=2, null=False, default="MF")
    stype = CharField(max_length=2, null=False, default="U")
    level = CharField(max_length=2, null=False, default="U")

    def __str__(self):
        return self.short_name

    def __unicode__(self):
        return self.short_name

# model to link schools with years
class SchoolStatistics(Model):
    school = ForeignKey(School)
    exam_year = IntegerField(db_index=True)
    div_name = CharField(max_length=10, null=False)
    div_count = IntegerField()

    def __str__(self):
        return str(self.school)