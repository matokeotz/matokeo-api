from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

# model for grades
class Grade(Model):
    letter = CharField(max_length=1, unique=True, db_index=True)
    value = IntegerField(unique=True)

    def __str__(self):
        return self.letter