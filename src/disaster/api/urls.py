from django.urls import path

from . import views


urlpatterns = [
    path('disaster/', views.DisasterListCreateAPIView.as_view(), name='api_disaster_cr'),
    path('disaster/<int:pk>', views.DisasterRetrieveUpdateDestroyAPIView.as_view(), name='api_disaster_cr'),
    path('disasterevent/', views.DisasterEventListCreateAPIView.as_view(), name='api_disasterevent_rud'),
    path('disasterevent/<int:pk>', views.DisasterEventRetrieveUpdateDestroyAPIView.as_view(), name='api_disasterevent_rud'),
]