from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField,\
	SlugRelatedField, HyperlinkedIdentityField
from rest_framework import serializers

from api.models.school_models import School, SchoolStatistics
from api.models.subject_models import SchoolSubject

# serializer for schools
class SchoolSerializer(ModelSerializer):

    class Meta:
        model = School
        fields = ('cno', 'short_name', 'long_name', 'gender', 'stype', 'level')

# serializer to link schools with aggregate grade stats
class SchoolStatisticsSerializer(ModelSerializer):
	school = SlugRelatedField(
		slug_field='short_name',
		read_only=True
	)

	class Meta:
		model = SchoolStatistics
		fields = ('school', 'exam_year')

# serializer to link schools with available subjects
class SchoolSubjectSerializer(ModelSerializer):
	school = SlugRelatedField(
		slug_field='short_name',
		read_only=True
	)
	subject = SlugRelatedField(
		slug_field='name',
		read_only=True
	)
	
	class Meta:
		model = SchoolSubject
		fields = ('school', 'subject')