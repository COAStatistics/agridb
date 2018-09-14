from rest_framework.serializers import ModelSerializer

from livestock.models import (
    Livestock,
    Investigation,
    CountType,
    Field,
    Profile,
)


class LivestockSerializer(ModelSerializer):

    class Meta:
        model = Livestock
        fields = '__all__'


class InvestigationSerializer(ModelSerializer):
    class Meta:
        model = Investigation
        fields = '__all__'


class CountTypeSerializer(ModelSerializer):
    class Meta:
        model = CountType
        fields = '__all__'


class FieldSerializer(ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
