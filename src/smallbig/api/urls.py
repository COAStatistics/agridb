from django.urls import path

from . import views


urlpatterns = [
    path('landlordretire/', views.LandlordRetireListCreateAPIView.as_view(), name='api_landlordretire_cr'),
    path('landlordrent/', views.LandlordRentListCreateAPIView.as_view(), name='api_landlordrent_cr'),
    path('tenanttransfer/', views.TenantTransferListCreateAPIView.as_view(), name='api_tenanttransfer_cr'),
    path('tenant/', views.TenantListCreateAPIView.as_view(), name='api_tenant_cr'),
    path('landlordretire_hash/', views.LandlordRetireHashListAPIView.as_view(), name='api_landlordretire_hash'),
    path('landlordrent_hash/', views.LandlordRentHashListAPIView.as_view(), name='api_landlordrent_hash'),
    path('tenanttransfer_hash/', views.TenantTransferHashListAPIView.as_view(), name='api_tenanttransfer_hash'),
    path('tenant_hash/', views.TenantHashListAPIView.as_view(), name='api_tenant_hash'),
    path('landlordretire/<int:pk>', views.LandlordRetireRetrieveUpdateDestroyAPIView.as_view(), name='api_landlordretire_rud'),
    path('landlordrent/<int:pk>', views.LandlordRentRetrieveUpdateDestroyAPIView.as_view(), name='api_landlordrent_rud'),
    path('tenanttransfer/<int:pk>', views.TenantTransferRetrieveUpdateDestroyAPIView.as_view(), name='api_tenanttransfer_rud'),
    path('tenant/<int:pk>', views.TenantRetrieveUpdateDestroyAPIView.as_view(), name='api_tenant_rud'),
]
