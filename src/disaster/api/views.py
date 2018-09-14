from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from disaster import models

from . import serializers


class DisasterListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DisasterSerializer
    queryset = models.Disaster.objects.all()
    permission_class = [IsAuthenticated]


class DisasterEventListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DisasterEventSerializer
    queryset = models.DisasterEvent.objects.all()
    permission_class = [IsAuthenticated]


class DisasterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DisasterSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.Disaster.objects.get(id=pk)
        return instance


class DisasterEventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DisasterEventSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.DisasterEvent.objects.get(id=pk)
        return instance