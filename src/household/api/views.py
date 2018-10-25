from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q

from household import models

from . import serializers


class ThousandPagination(pagination.PageNumberPagination):
    page_size = 2


class HouseholdListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.HouseholdSerializer
    queryset = models.Household.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['household_number']

    def initial(self, request, *args, **kwargs):
        super(HouseholdListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.page = request.query_params.get('page', None)
        self.household_number = request.query_params.get('household_number', None)
        self.address = request.query_params.get('address', None)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.household_number is not None:
            queryset = queryset.filter(household_number__icontains=self.household_number)
        if self.address is not None:
            queryset = queryset.filter(address__icontains=self.address)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
