from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField,\
    SlugRelatedField, HyperlinkedIdentityField
from rest_framework import serializers

from api.models.grade_models import Grade

class GradeSerializer(ModelSerializer):

    class Meta:
        model = Grade
        fields = ('letter', 'value')