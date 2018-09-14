from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from disaster.models import (
    DisasterEvent,
    Disaster,
)


class DisasterSerializer(ModelSerializer):

    class Meta:
        model = Disaster
        fields = '__all__'


class DisasterEventSerializer(ModelSerializer):

    class Meta:
        model = DisasterEvent
        fields = '__all__'
