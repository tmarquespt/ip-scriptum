from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),

    # VLANS
    path('vlans/', VLANListView.as_view(), name='vlan_list'),
    path('vlans/add/', VLANCreateView.as_view(), name='vlan_add'),
    path('vlans/<int:pk>/edit/', VLANUpdateView.as_view(), name='vlan_edit'),

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

    path('devices/', GeneralDeviceListView.as_view(), name='device_list'),






]
