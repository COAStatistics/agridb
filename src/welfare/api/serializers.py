from rest_framework.serializers import ModelSerializer

from welfare.models import (
    ElderlyAllowance,
    FarmerInsurance,
    Scholarship,
)


class ElderlyAllowanceSerializer(ModelSerializer):

    class Meta:
        model = ElderlyAllowance
        fields = '__all__'


class FarmerInsuranceSerializer(ModelSerializer):

    class Meta:
        model = FarmerInsurance
        fields = '__all__'


class ScholarshipSerializer(ModelSerializer):

    class Meta:
        model = Scholarship
        fields = '__all__'

