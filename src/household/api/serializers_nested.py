from rest_framework import serializers
from livestock.api.serializers_nested import FieldSerializer
from household import models


class MemberSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = models.Member
        fields = ['name', 'app_id', 'fields']