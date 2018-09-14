from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from fallow.models import (
    Crop,
    Declare,
    RiceArea,
    FallowTransfer,
    TransferCrop
)


class CropSerializers(ModelSerializer):

    class Meta:
        model = Crop
        fields = '__all__'


class DeclareSerializers(ModelSerializer):

    class Meta:
        model = Declare
        fields = '__all__'


class RiceAreaSerializers(ModelSerializer):

    class Meta:
        model = RiceArea
        fields = '__all__'


class FallowTransferSerializers(ModelSerializer):

    class Meta:
        model = FallowTransfer
        fields = '__all__'


class TransferCropSerializers(ModelSerializer):

    class Meta:
        model = TransferCrop
        fields = '__all__'
