from django.urls import path

from . import views


urlpatterns = [
    path('crop/', views.CropListCreateAPIView.as_view(), name='api_crop_cr'),
    path('declare/', views.DeclareListCreateAPIView.as_view(), name='api_declare_cr'),
    path('ricearea/', views.RiceAreaListCreateAPIView.as_view(), name='api_ricearea_cr'),
    path('fallowtransfer/', views.FallowTransferListCreateAPIView.as_view(), name='api_fallowtransfer_cr'),
    path('transfercrop/', views.TransferCropListCreateAPIView.as_view(), name='api_transfercrop_cr'),
    path('crop/<int:pk>', views.CropRetrieveUpdateDestroyAPIView.as_view(), name='api_crop_rud'),
    path('declare/<int:pk>', views.DeclareRetrieveUpdateDestroyAPIView.as_view(), name='api_declare_rud'),
    path('ricearea/<int:pk>', views.RiceAreaRetrieveUpdateDestroyAPIView.as_view(), name='api_ricearea_rud'),
    path('fallowtransfer/<int:pk>', views.FallowTransferRetrieveUpdateDestroyAPIView.as_view(), name='api_fallowtransfer_rud'),
    path('transfercrop/<int:pk>', views.TransferCropRetrieveUpdateDestroyAPIView.as_view(), name='api_transfercrop_rud'),

]
