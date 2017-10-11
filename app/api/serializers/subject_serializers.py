from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField,\
    SlugRelatedField, HyperlinkedIdentityField
from rest_framework import serializers

from api.models.subject_models import Subject, SubjectGradeStatistics

class SubjectSerializer(ModelSerializer):

    class Meta:
        model = Subject
        fields = ('code', 'name', 'is_required')

class SubjectGradeStatisticsSerializer(ModelSerializer):
    school = StringRelatedField()
    subject = StringRelatedField()
    grade = StringRelatedField()

    class Meta:
        model = SubjectGradeStatistics
        fields = ('grade', 'exam_year', 'school', 'subject', 'student_count', 'gender')