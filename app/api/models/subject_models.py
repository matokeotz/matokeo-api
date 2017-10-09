from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

from api.models.school_models import School
from api.models.grade_models import Grade

class Subject(Model):
    '''
        Stores information on a single subject
    '''

    code = CharField(max_length=20, null=False, unique=True, db_index=True)
    name = CharField(max_length=100, null= False, unique=True)
    is_required = BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class SubjectGradeStatistics(Model):
    '''
        Stores the aggregate grade information
        for a specific subject in a specific
        school in a specific year. Relates 
        :model:`api.School`, :model:`api.Subject`,
        and :model:`api.Grade`.
    '''

    school = ForeignKey(School)
    subject = ForeignKey(Subject)
    grade = ForeignKey(Grade)
    exam_year = IntegerField()
    student_count = IntegerField()
    gender = CharField(max_length=2)

    def __str__(self):
        return str(self.subject)