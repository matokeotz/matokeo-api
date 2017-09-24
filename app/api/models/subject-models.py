from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

# model for subjects
class Subject(Model):
    code = CharField(max_length=20, null=False, unique=True, db_index=True)
    name = CharField(max_length=100, null= False, unique=True)
    is_required = BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/subject/'+ self.name.lower() + '/'

# model to link subject with grades and statistics
class SubjectGradeStatistics(Model):
    grade = ForeignKey(Grade)
    exam_year = IntegerField()
    school = ForeignKey(School)
    subject = ForeignKey(Subject)
    student_count = IntegerField()
    gender = CharField(max_length=2)