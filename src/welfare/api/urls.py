from django.urls import path

from . import views


urlpatterns = [
    path('elderlyallowance/', views.ElderlyAllowanceListCreateAPIView.as_view(), name='api_elderlyallowance_cr'),
    path('farmerinsurance/', views.FarmerInsuranceListCreateAPIView.as_view(), name='api_farmerinsurance_cr'),
    path('scholarship/', views.ScholarshipListCreateAPIView.as_view(), name='api_scholarship_cr'),
    path('elderlyallowance/<int:pk>', views.ElderlyAllowanceRetrieveUpdateDestroyAPIView.as_view(), name='api_elderlyallowance_rud'),
    path('farmerinsurance/<int:pk>', views.FarmerInsuranceRetrieveUpdateDestroyAPIView.as_view(), name='api_farmerinsurance_rud'),
    path('scholarship/<int:pk>', views.ScholarshipRetrieveUpdateDestroyAPIView.as_view(), name='api_scholarship_rud'),
]
