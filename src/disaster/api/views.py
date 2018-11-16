from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q

from household.api.views import ThousandPagination
from household.models import Member

from fallow.models import Crop

from disaster import models

from . import serializers


class DisasterListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DisasterSerializer
    queryset = models.Disaster.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def initial(self, request, *args, **kwargs):
        super(DisasterListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.page = request.query_params.get('page', None)
        self.member = request.query_params.get('member', '')
        self.event = request.query_params.get('event', '')
        self.crop = request.query_params.get('crop', '')
        self.area = request.query_params.get('area', '')
        self.subsidy = request.query_params.get('subsidy', '')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.member is not '':
            member = Member.objects.filter(app_id__icontains=self.member)
            queryset = queryset.filter(member__in=member)

        if self.event is not '':
            event = models.DisasterEvent.objects.filter(name__icontains=self.event)
            queryset = queryset.filter(event__in=event)

        if self.crop is not '':
            crop = Crop.objects.filter(name__icontains=self.crop)
            queryset = queryset.filter(crop__in=crop)

        queryset = queryset.filter(
            Q(area__icontains=self.area) &
            Q(subsidy__icontains=self.subsidy)
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DisasterEventListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DisasterEventSerializer
    queryset = models.DisasterEvent.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def initial(self, request, *args, **kwargs):
        super(DisasterEventListCreateAPIView, self).initial(request, *args, **kwargs)

        # setting
        self.page = request.query_params.get('page', None)
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


class DisasterEventHashListAPIView(generics.ListAPIView):
    serializer_class = serializers.DisasterEventSerializer
    queryset = models.DisasterEvent.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {}
            for i in serializer.data:
                data[i['name']] = i['id']
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = {}
        for i in serializer.data:
            data[i['name']] = i['id']

        return Response(data)


class DisasterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DisasterSerializer
    queryset = models.Disaster.objects.all()
    permission_classes = [IsAuthenticated]


class DisasterEventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DisasterEventSerializer
    queryset = models.DisasterEvent.objects.all()
    permission_classes = [IsAuthenticated]
