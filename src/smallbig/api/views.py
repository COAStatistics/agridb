from . import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from smallbig import models


class LandlordRetireListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.LandlordRetireSerializer
    queryset = models.LandlordRetire.objects.all()
    permission_class = [IsAuthenticated]


class LandlordRentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.LandlordRentSerializer
    queryset = models.LandlordRent.objects.all()
    permission_class = [IsAuthenticated]


class TenantTransferListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TenantTransferSerializer
    queryset = models.TenantTransfer.objects.all()
    permission_class = [IsAuthenticated]


class TenantListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TenantSerializer
    queryset = models.Tenant.objects.all()
    permission_class = [IsAuthenticated]


class LandlordRetireRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LandlordRetireSerializer
    queryset = models.LandlordRetire.objects.all()
    permission_class = [IsAuthenticated]


class LandlordRentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LandlordRentSerializer
    queryset = models.LandlordRent.objects.all()
    permission_class = [IsAuthenticated]


class TenantTransferRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TenantTransferSerializer
    queryset = models.TenantTransfer.objects.all()
    permission_class = [IsAuthenticated]


class TenantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TenantSerializer
    queryset = models.Tenant.objects.all()
    permission_class = [IsAuthenticated]
