from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from fallow.models import (
    Crop,
    Declare,
    RiceArea,
    FallowTransfer,
    TransferCrop,
)
from . import serializers


class CropListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CropSerializers
    queryset = Crop.objects.all()
    permission_class = [IsAuthenticated]


class DeclareListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DeclareSerializers
    queryset = Declare.objects.all()
    permission_class = [IsAuthenticated]


class RiceAreaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.RiceAreaSerializers
    queryset = RiceArea.objects.all()
    permission_class = [IsAuthenticated]


class FallowTransferListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.FallowTransferSerializers
    queryset = FallowTransfer.objects.all()
    permission_class = [IsAuthenticated]


class TransferCropListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TransferCropSerializers
    queryset = TransferCrop.objects.all()
    permission_class = [IsAuthenticated]


class CropRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CropSerializers
    queryset = Crop.objects.all()
    permission_class = [IsAuthenticated]


class DeclareRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DeclareSerializers
    queryset = Declare.objects.all()
    permission_class = [IsAuthenticated]


class RiceAreaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RiceAreaSerializers
    queryset = RiceArea.objects.all()
    permission_class = [IsAuthenticated]


class FallowTransferRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FallowTransferSerializers
    queryset = FallowTransfer.objects.all()
    permission_class = [IsAuthenticated]


class TransferCropRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TransferCropSerializers
    queryset = TransferCrop.objects.all()
    permission_class = [IsAuthenticated]
