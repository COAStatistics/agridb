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
    page_size = 1000


class HouseholdListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.HouseholdSerializer
    queryset = models.Household.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['household_number']

    def initial(self, request, *args, **kwargs):
        super(HouseholdListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.page = request.query_params.get('page', None)
        self.household_number = request.query_params.get('household_number', '')
        self.address = request.query_params.get('address', '')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        queryset = queryset.filter(
            Q(household_number__icontains=self.household_number) &
            Q(address__icontains=self.address)
        )

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
    pagination_class = ThousandPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']

    def initial(self, request, *args, **kwargs):
        super(RoleListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.name = request.query_params.get('name', '')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        queryset = queryset.filter(name__icontains=self.name)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MemberListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.MemberSerializer
    queryset = models.Member.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']

    def initial(self, request, *args, **kwargs):
        super(MemberListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.page = request.query_params.get('page', None)
        self.household = request.query_params.get('household', '')
        self.role = request.query_params.get('role', '')
        self.name = request.query_params.get('name', None)
        self.app_id = request.query_params.get('app_id', '')
        self.code = request.query_params.get('code', '')
        self.birth = request.query_params.get('birth', '')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.household is not '':
            household = models.Household.objects.filter(household_number__icontains=self.household)
            queryset = queryset.filter(household__in=household)

        if self.role is not '':
            role = models.Role.objects.filter(name__icontains=self.role)
            queryset = queryset.filter(role__in=role)

        if self.name is not None:
            queryset = queryset.filter(
                Q(name__icontains=self.name) &
                Q(app_id__icontains=self.app_id) &
                Q(code__icontains=self.code) &
                Q(birth__icontains=self.birth)
            )
        else:
            queryset = queryset.filter(
                Q(name__isnull=True) |
                Q(name__isnull=False)
            ).filter(
                Q(app_id__icontains=self.app_id) &
                Q(code__icontains=self.code) &
                Q(birth__icontains=self.birth)
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
