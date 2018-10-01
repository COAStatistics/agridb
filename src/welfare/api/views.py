from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from welfare.models import (
    ElderlyAllowance,
    FarmerInsurance,
    Scholarship,
)
from . import serializers


class ElderlyAllowanceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.ElderlyAllowanceSerializer
    queryset = ElderlyAllowance.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class FarmerInsuranceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.FarmerInsuranceSerializer
    queryset = FarmerInsurance.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class ScholarshipListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.ScholarshipSerializer
    queryset = Scholarship.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'subsidy']


class ElderlyAllowanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ElderlyAllowanceSerializer
    queryset = ElderlyAllowance.objects.all()
    permission_classes = [IsAuthenticated]


class FarmerInsuranceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FarmerInsuranceSerializer
    queryset = FarmerInsurance.objects.all()
    permission_classes = [IsAuthenticated]


class ScholarshipRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ScholarshipSerializer
    queryset = Scholarship.objects.all()
    permission_classes = [IsAuthenticated]
