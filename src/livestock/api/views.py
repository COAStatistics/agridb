from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from livestock import models

from . import serializers


class LivestockListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.LivestockSerializer
    queryset = models.Livestock.objects.all()
    permission_classes = [IsAuthenticated]


class LivestockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LivestockSerializer
    queryset = models.Livestock.objects.all()
    permission_classes = [IsAuthenticated]


class InvestigationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.InvestigationSerializer
    queryset = models.Investigation.objects.all()
    permission_classes = [IsAuthenticated]


class InvestigationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.InvestigationSerializer
    queryset = models.Investigation.objects.all()
    permission_classes = [IsAuthenticated]


class CountTypeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CountTypeSerializer
    queryset = models.CountType.objects.all()
    permission_classes = [IsAuthenticated]


class CountTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CountTypeSerializer
    queryset = models.CountType.objects.all()
    permission_classes = [IsAuthenticated]


class FieldListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.FieldSerializer
    queryset = models.Field.objects.all()
    permission_classes = [IsAuthenticated]


class FieldRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FieldSerializer
    queryset = models.Field.objects.all()
    permission_classes = [IsAuthenticated]


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()
    permission_classes = [IsAuthenticated]


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()
    permission_classes = [IsAuthenticated]
