from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from livestock import models
from household.models import Member
from household.api.serializers import MemberSerializer
from household.api.views import ThousandPagination

from . import serializers


class LivestockListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.LivestockSerializer
    queryset = models.Livestock.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class LivestockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LivestockSerializer
    queryset = models.Livestock.objects.all()
    permission_classes = [IsAuthenticated]


class InvestigationTypeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.InvestigationTypeSerializer
    queryset = models.InvestigationType.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class InvestigationTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.InvestigationTypeSerializer
    queryset = models.InvestigationType.objects.all()
    permission_classes = [IsAuthenticated]


class InvestigationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.InvestigationSerializer
    queryset = models.Investigation.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class InvestigationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.InvestigationSerializer
    queryset = models.Investigation.objects.all()
    permission_classes = [IsAuthenticated]


class CountTypeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CountTypeSerializer
    queryset = models.CountType.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class CountTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CountTypeSerializer
    queryset = models.CountType.objects.all()
    permission_classes = [IsAuthenticated]


class FieldListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.FieldSerializer
    queryset = models.Field.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class FieldRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FieldSerializer
    queryset = models.Field.objects.all()
    permission_classes = [IsAuthenticated]


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()
    permission_classes = [IsAuthenticated]


# hash api

class LivestockHashListAPIView(generics.ListAPIView):
    serializer_class = serializers.LivestockSerializer
    queryset = models.Livestock.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        paginate_queryset = self.paginate_queryset(queryset)

        if paginate_queryset is not None:
            response = self.get_paginated_response
            queryset = paginate_queryset
        else:
            response = Response

        serializer = self.get_serializer(queryset, many=True)
        data = {}
        for i in serializer.data:
            data[i['full_code']] = i['id']

        return response(data)


class LivestockResult(generics.ListAPIView):
    serializer_class = serializers.LivestockResultSerializer
    queryset = models.Profile.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['member__name', 'member__app_id']