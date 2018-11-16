from django.urls import path

from . import views


urlpatterns = [
    path('disaster/', views.DisasterListCreateAPIView.as_view(), name='api_disaster_cr'),
    path('disaster/<int:pk>', views.DisasterRetrieveUpdateDestroyAPIView.as_view(), name='api_disaster_rud'),
    path('disasterevent_hash/', views.DisasterEventHashListAPIView.as_view(), name='api_disasterevent_hash'),
    path('disasterevent/', views.DisasterEventListCreateAPIView.as_view(), name='api_disasterevent_cr'),
    path('disasterevent/<int:pk>', views.DisasterEventRetrieveUpdateDestroyAPIView.as_view(), name='api_disasterevent_rud'),
]
