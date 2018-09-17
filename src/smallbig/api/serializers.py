from rest_framework.serializers import ModelSerializer
from smallbig import models


class LandlordRetireSerializer(ModelSerializer):

    class Meta:
        model = models.LandlordRetire
        fields = '__all__'


class LandlordRentSerializer(ModelSerializer):

    class Meta:
        model = models.LandlordRent
        fields = '__all__'


class TenantTransferSerializer(ModelSerializer):

    class Meta:
        model = models.TenantTransfer
        fields = '__all__'


class TenantSerializer(ModelSerializer):

    class Meta:
        model = models.Tenant
        fields = '__all__'
