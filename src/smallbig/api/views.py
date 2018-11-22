from . import serializers
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from smallbig import models
from household.api.views import ThousandPagination


class LandlordRetireListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.LandlordRetireSerializer
    queryset = models.LandlordRetire.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class LandlordRentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.LandlordRentSerializer
    queryset = models.LandlordRent.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class TenantTransferListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TenantTransferSerializer
    queryset = models.TenantTransfer.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class TenantListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TenantSerializer
    queryset = models.Tenant.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.member = request.POST['member'] or None
        self.owner = request.POST['owner'] or None
        self.year = request.POST['year'] or 1
        if models.Tenant.objects.filter(member=self.member, owner=self.owner, year=self.year).exists():
            return Response("The fields member, owner, year must make a unique set.")

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LandlordRetireHashListAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.LandlordRetireSerializer
    queryset = models.LandlordRetire.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {}
            for i in serializer.data:
                data[i['member']] = i['id']
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = {}
        for i in serializer.data:
            data[i['member']] = i['id']

        return Response(data)


class LandlordRentHashListAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.LandlordRentSerializer
    queryset = models.LandlordRent.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {}
            for i in serializer.data:
                data[i['member']] = i['id']
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = {}
        for i in serializer.data:
            data[i['member']] = i['id']

        return Response(data)


class TenantTransferHashListAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TenantTransferSerializer
    queryset = models.TenantTransfer.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {}
            for i in serializer.data:
                data[i['member']] = i['id']
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = {}
        for i in serializer.data:
            data[i['member']] = i['id']

        return Response(data)


class TenantHashListAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TenantSerializer
    queryset = models.Tenant.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {}
            for i in serializer.data:
                data[i['member']] = i['id']
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = {}
        for i in serializer.data:
            data[i['member']] = i['id']

        return Response(data)


class LandlordRetireRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LandlordRetireSerializer
    queryset = models.LandlordRetire.objects.all()
    permission_classes = [IsAuthenticated]


class LandlordRentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LandlordRentSerializer
    queryset = models.LandlordRent.objects.all()
    permission_classes = [IsAuthenticated]


class TenantTransferRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TenantTransferSerializer
    queryset = models.TenantTransfer.objects.all()
    permission_classes = [IsAuthenticated]


class TenantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TenantSerializer
    queryset = models.Tenant.objects.all()
    permission_classes = [IsAuthenticated]
