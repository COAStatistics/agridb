from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from household import models

from . import serializers


class HouseholdListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.HouseholdSerializer
    queryset = models.Household.objects.all()
    permission_class = [IsAuthenticated]


class RoleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()
    permission_class = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']


class MemberListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.MemberSerializer
    queryset = models.Member.objects.all()
    permission_class = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        household = models.Household.objects.get(household_number=request.data['household'])
        role = models.Role.objects.get(name=request.data['role'])
        app_id = request.data['app_id']
        name = request.data['name']
        data = {
            'household': household.id,
            'role': role.id,
            'app_id': app_id,
            'name': name,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class HouseholdRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.HouseholdSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.Household.objects.get(id=pk)
        return instance


class RoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RoleSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.Role.objects.get(id=pk)
        return instance


class MemberRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MemberSerializer
    permission_class = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = models.Member.objects.get(id=pk)
        return instance
