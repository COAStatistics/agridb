from django.urls import path

from . import views


urlpatterns = [
    path('landlordretire/', views.LandlordRetireListCreateAPIView.as_view(), name='api_landlordretire_cr'),
    path('landlordrent/', views.LandlordRentListCreateAPIView.as_view(), name='api_landlordrent_cr'),
    path('tenanttransfer/', views.TenantTransferListCreateAPIView.as_view(), name='api_tenanttransfer_cr'),
    path('tenant/', views.TenantListCreateAPIView.as_view(), name='api_tenant_cr'),
    path('landlordretire/<int:pk>', views.LandlordRetireRetrieveUpdateDestroyAPIView.as_view(), name='api_landlordretire_rud'),
    path('landlordrent/<int:pk>', views.LandlordRentRetrieveUpdateDestroyAPIView.as_view(), name='api_landlordrent_rud'),
    path('tenanttransfer/<int:pk>', views.TenantTransferRetrieveUpdateDestroyAPIView.as_view(), name='api_tenanttransfer_rud'),
    path('tenant/<int:pk>', views.TenantRetrieveUpdateDestroyAPIView.as_view(), name='api_tenant_rud'),
]
