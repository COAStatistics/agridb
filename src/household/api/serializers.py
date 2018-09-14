from rest_framework import serializers

from household import models


class HouseholdSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Household
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Role
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Member
        fields = '__all__'
