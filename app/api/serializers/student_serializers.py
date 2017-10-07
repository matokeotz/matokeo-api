from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField,\
    SlugRelatedField, HyperlinkedIdentityField
from rest_framework import serializers

from api.models.student_models import Student

class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ('identifier', 'gender', 'aggregate_score', 'graduation_year', 'division', 'school')