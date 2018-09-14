from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from household import models
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
    serializer_class = serializers.TransferCrop
    queryset = TransferCrop.objects.all()
    permission_class = [IsAuthenticated]


class CropRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CropSerializers
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = Crop.objects.get(id=pk)
        return instance


class DeclareRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DeclareSerializers
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = Declare.objects.get(id=pk)
        return instance


class RiceAreaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RiceAreaSerializers
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = RiceArea.objects.get(id=pk)
        return instance


class FallowTransferRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FallowTransferSerializers
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = FallowTransfer.objects.get(id=pk)
        return instance


class TransferCropRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TransferCropSerializers
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = TransferCrop.objects.get(id=pk)
        return instance
