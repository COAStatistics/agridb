from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from household import models

from . import serializers


class HouseholdListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.HouseholdSerializer
    queryset = models.Household.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['household_number']


class RoleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']


class MemberListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.MemberSerializer
    queryset = models.Member.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']


class HouseholdRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.HouseholdSerializer
    queryset = models.Household.objects.all()
    permission_classes = [IsAuthenticated]


class RoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()
    permission_classes = [IsAuthenticated]


class MemberRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MemberSerializer
    queryset = models.Member.objects.all()
    permission_classes = [IsAuthenticated]
