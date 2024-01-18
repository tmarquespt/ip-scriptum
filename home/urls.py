from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),

    # NETWORKS
    path('networks/', NETWORKListView.as_view(), name='network_list'),
    path('networks/add/', NETWORKCreateView.as_view(), name='network_add'),
    path('networks/<int:pk>/edit/', NETWORKUpdateView.as_view(), name='network_edit'),

    #SSIDs
    path('ssids/', SSIDListView.as_view(), name='ssid_list'),
    path('ssids/add/', SSIDCreateView.as_view(), name='ssid_add'),
    path('ssids/<int:pk>/edit/', SSIDUpdateView.as_view(), name='ssid_edit'),

    # ClientDevice URLs
    path('client-devices/', ClientDeviceListView.as_view(), name='client_device_list'),
    path('client-devices/add/', ClientDeviceCreateView.as_view(), name='client_device_add'),
    path('client-devices/<int:pk>/edit/', ClientDeviceUpdateView.as_view(), name='client_device_edit'),
    
    # NetworkInfrastructureDevice URLs
    path('network-devices/', NetworkInfrastructureDeviceListView.as_view(), name='network_infrastructure_device_list'),
    path('network-devices/add/', NetworkInfrastructureDeviceCreateView.as_view(), name='network_infrastructure_device_add'),
    path('network-devices/<int:pk>/edit/', NetworkInfrastructureDeviceUpdateView.as_view(), name='network_infrastructure_device_edit'),
    path('networks/<int:pk>/delete/', NETWORKDeleteView.as_view(), name='network_delete'),

    path('devices/', GeneralDeviceListView.as_view(), name='device_list'),

    #SET CURRENT SITE
    path('set-current-site/', views.set_current_site, name='set_current_site'),
]





