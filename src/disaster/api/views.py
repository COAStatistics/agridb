from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from household.api.views import ThousandPagination
from disaster import models

from . import serializers


class DisasterListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DisasterSerializer
    queryset = models.Disaster.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class DisasterEventListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DisasterEventSerializer
    queryset = models.DisasterEvent.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class DisasterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DisasterSerializer
    queryset = models.Disaster.objects.all()
    permission_classes = [IsAuthenticated]


class DisasterEventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DisasterEventSerializer
    queryset = models.DisasterEvent.objects.all()
    permission_classes = [IsAuthenticated]
