from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

class TestStudent(Model):
    test_id = CharField(max_length=15)

    def __str__(self):
        return self.test_id