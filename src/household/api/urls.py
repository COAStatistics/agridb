from django.urls import path

from . import views


urlpatterns = [
    path('household/', views.HouseholdListCreateAPIView.as_view(), name='api_household_cr'),
    path('role/', views.RoleListCreateAPIView.as_view(), name='api_role_cr'),
    path('member/', views.MemberListCreateAPIView.as_view(), name='api_member_cr'),
    path('household/<int:pk>', views.HouseholdRetrieveUpdateDestroyAPIView.as_view(), name='api_household_rud'),
    path('role/<int:pk>', views.RoleRetrieveUpdateDestroyAPIView.as_view(), name='api_role_rud'),
    path('member/<int:pk>', views.MemberRetrieveUpdateDestroyAPIView.as_view(), name='api_member_rud'),
]
