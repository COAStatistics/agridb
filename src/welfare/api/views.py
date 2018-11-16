from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q

from household.api.views import ThousandPagination
from household.models import Member

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
    pagination_class = ThousandPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    def initial(self, request, *args, **kwargs):
        super(ElderlyAllowanceListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.page = request.query_params.get('page', None)
        self.member = request.query_params.get('member', '')
        self.year = request.query_params.get('year', '')
        self.subsidy = request.query_params.get('subsidy', '')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.member is not '':
            member = models.member.objects.filter(app_id__icontains=self.member)
            queryset = queryset.filter(member__in=member)

        if self.year is not '':
            year = models.Year.objects.filter(year__icontains=self.year)
            queryset = queryset.filter(year__in=year)

        queryset = queryset.filter(subsidy__icontains=self.subsidy)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FarmerInsuranceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.FarmerInsuranceSerializer
    queryset = FarmerInsurance.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    def initial(self, request, *args, **kwargs):
        super(FarmerInsuranceListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.page = request.query_params.get('page', None)
        self.member = request.query_params.get('member', '')
        self.year = request.query_params.get('year', '')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.member is not '':
            member = models.member.objects.filter(app_id__icontains=self.member)
            queryset = queryset.filter(member__in=member)

        if self.year is not '':
            year = models.Year.objects.filter(year__icontains=self.year)
            queryset = queryset.filter(year__in=year)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ScholarshipListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.ScholarshipSerializer
    queryset = Scholarship.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'subsidy']

    def initial(self, request, *args, **kwargs):
        super(ElderlyAllowanceListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.page = request.query_params.get('page', None)
        self.member = request.query_params.get('member', '')
        self.year = request.query_params.get('year', '')
        self.name = request.query_params.get('name', '')
        self.subsidy = request.query_params.get('subsidy', '')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.member is not '':
            member = models.member.objects.filter(app_id__icontains=self.member)
            queryset = queryset.filter(member__in=member)

        if self.year is not '':
            year = models.Year.objects.filter(year__icontains=self.year)
            queryset = queryset.filter(year__in=year)

        queryset = queryset.filter(
            Q(subsidy__icontains=self.subsidy) &
            Q(name__icontains=self.name)
        )
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
