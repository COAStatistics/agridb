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
    permission_class = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class FarmerInsuranceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.FarmerInsuranceSerializer
    queryset = FarmerInsurance.objects.all()
    permission_class = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class ScholarshipListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.ScholarshipSerializer
    queryset = Scholarship.objects.all()
    permission_class = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'subsidy']


class ElderlyAllowanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ElderlyAllowanceSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = ElderlyAllowance.objects.get(id=pk)
        return instance


class FarmerInsuranceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FarmerInsuranceSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = FarmerInsurance.objects.get(id=pk)
        return instance


class ScholarshipRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ScholarshipSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = Scholarship.objects.get(id=pk)
        return instance
