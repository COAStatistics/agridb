from django.urls import path

from . import views


urlpatterns = [
    path('household/', views.HouseholdListCreateAPIView.as_view(), name='api_household_cr'),
    path('role/', views.RoleListCreateAPIView.as_view(), name='api_role_cr'),
    path('member/', views.MemberListCreateAPIView.as_view(), name='api_member_cr'),
    path('year/', views.YearListCreateAPIView.as_view(), name='api_year_cr'),
    path('household_hash/', views.HouseholdHashListAPIView.as_view(), name='api_household_hash'),
    path('role_hash/', views.RoleHashListAPIView.as_view(), name='api_role_hash'),
    path('member_hash/', views.MemberHashListAPIView.as_view(), name='api_member_hash'),
    path('year_hash/', views.YearHashListAPIView.as_view(), name='api_year_hash'),
    path('household/<int:pk>', views.HouseholdRetrieveUpdateDestroyAPIView.as_view(), name='api_household_rud'),
    path('role/<int:pk>', views.RoleRetrieveUpdateDestroyAPIView.as_view(), name='api_role_rud'),
    path('member/<int:pk>', views.MemberRetrieveUpdateDestroyAPIView.as_view(), name='api_member_rud'),
    path('year/<int:pk>', views.YearRetrieveUpdateDestroyAPIView.as_view(), name='api_year_rud'),
    # nested
    path('member_nested/', views.MemberNestedListAPIView.as_view(), name='api_member_nested'),
]
