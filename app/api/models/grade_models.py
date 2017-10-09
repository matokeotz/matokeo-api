from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

class Grade(Model):
    '''
        Stores information on a single grade
    '''

    letter = CharField(max_length=1, unique=True, db_index=True)
    value = IntegerField(unique=True)

    def __str__(self):
        return self.letter