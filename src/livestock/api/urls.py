from django.urls import path

from . import views

urlpatterns = [
    path('livestock/', views.LivestockListCreateAPIView.as_view(), name='api_livestock_cr'),
    path('investigation/', views.InvestigationListCreateAPIView.as_view(), name='api_investigation_cr'),
    path('investigationtype/', views.InvestigationTypeListCreateAPIView.as_view(), name='api_investigationtype_cr'),
    path('counttype/', views.CountTypeListCreateAPIView.as_view(), name='api_counttype_cr'),
    path('field/', views.FieldListCreateAPIView.as_view(), name='api_field_cr'),
    path('profile/', views.ProfileListCreateAPIView.as_view(), name='api_profile_cr'),
    path('livestock/<int:pk>', views.LivestockRetrieveUpdateDestroyAPIView.as_view(), name='api_livestock_rud'),
    path('investigation/<int:pk>', views.InvestigationRetrieveUpdateDestroyAPIView.as_view(), name='api_investigation_rud'),
    path('investigationtype/<int:pk>', views.InvestigationTypeRetrieveUpdateDestroyAPIView.as_view(), name='api_investigationtype_rud'),
    path('counttype/<int:pk>', views.CountTypeRetrieveUpdateDestroyAPIView.as_view(), name='api_counttype_rud'),
    path('field/<int:pk>', views.FieldRetrieveUpdateDestroyAPIView.as_view(), name='api_field_rud'),
    path('profile/<int:pk>', views.ProfileRetrieveUpdateDestroyAPIView.as_view(), name='api_profile_rud'),
    path('livestock_hash/', views.LivestockHashListAPIView.as_view(), name='api_livestock_hash'),
    # api view
    path('livestock_result/', views.LivestockResult.as_view(), name='api_livestock_result'),
]
