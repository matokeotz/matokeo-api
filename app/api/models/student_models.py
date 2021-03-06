from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, BooleanField, DateTimeField

from api.models.school_models import School
from api.models.subject_models import Subject
from api.models.grade_models import Grade

# model for students
class Student(Model):
    '''
        Stores information on a single student
        Relates to :model:`api.School`.
    '''

    identifier = CharField(max_length=15)
    gender = CharField(max_length=2)
    aggregate_score = IntegerField(db_index=True)
    graduation_year = IntegerField(db_index=True)
    division = CharField(max_length=5)
    school = ForeignKey(School)

    def __str__(self):
        return self.identifier

# model to link students with subjects and grades
class StudentSubjectGrade(Model):
    '''
        Stores the grade of a specific student for
        a specific subject. Relates
        :model:`api.Student`, :model:`api.Subject`,
        and :model:`api.Grade`.
    '''

    student = ForeignKey(Student)
    subject = ForeignKey(Subject)
    grade = ForeignKey(Grade)

    def __str__(self):
        return str(self.student)