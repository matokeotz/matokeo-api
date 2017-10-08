from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField,\
    SlugRelatedField, HyperlinkedIdentityField
from rest_framework import serializers

from api.models.student_models import Student, StudentSubjectGrade

class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ('identifier', 'gender', 'aggregate_score', 'graduation_year', 'division', 'school')

class StudentSubjectGradeSerializer(ModelSerializer):
    student = StringRelatedField()
    subject = StringRelatedField()
    grade = StringRelatedField()

    class Meta:
        model = StudentSubjectGrade
        fields = ('student', 'subject', 'grade')

class SchoolStudentSerializer(ModelSerializer):
    school = StringRelatedField()

    class Meta:
        model = Student
        fields = ('school', 'graduation_year', 'gender', 'division', 'aggregate_score')