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
    permission_class = [IsAuthenticated]


class LivestockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LivestockSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.Livestock.objects.get(id=pk)
        return instance


class InvestigationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.InvestigationSerializer
    queryset = models.Investigation.objects.all()
    permission_class = [IsAuthenticated]


class InvestigationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.InvestigationSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.Investigation.objects.get(id=pk)
        return instance


class CountTypeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CountTypeSerializer
    queryset = models.CountType.objects.all()
    permission_class = [IsAuthenticated]


class CountTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CountTypeSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.CountType.objects.get(id=pk)
        return instance


class FieldListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.FieldSerializer
    queryset = models.Field.objects.all()
    permission_class = [IsAuthenticated]


class FieldRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FieldSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.Field.objects.get(id=pk)
        return instance


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()
    permission_class = [IsAuthenticated]


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProfileSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.Profile.objects.get(id=pk)
        return instance

