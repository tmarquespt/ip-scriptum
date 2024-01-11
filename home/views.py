from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

################################################
#
# VLANs
#
###############################################



class VLANListView(ListView):
    model = VLAN
    template_name = 'pages/vlan_list.html'
    context_object_name = 'vlans'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return VLAN.objects.filter(name__icontains=query)
        return VLAN.objects.all()

class VLANCreateView(CreateView):
    model = VLAN
    form_class = VLANForm
    template_name = 'pages/vlan_form.html'
    success_url = reverse_lazy('vlan_list')

class VLANUpdateView(UpdateView):
    model = VLAN
    form_class = VLANForm
    template_name = 'pages/vlan_form.html'
    success_url = reverse_lazy('vlan_list')

################################################
#
# SSIDs
#
###############################################

class SSIDListView(ListView):
    model = SSID
    template_name = 'pages/ssid_list.html'
    context_object_name = 'ssids'

class SSIDCreateView(CreateView):
    model = SSID
    form_class = SSIDForm
    template_name = 'pages/ssid_form.html'
    success_url = reverse_lazy('ssid_list')

class SSIDUpdateView(UpdateView):
    model = SSID
    form_class = SSIDForm
    template_name = 'pages/ssid_form.html'
    success_url = reverse_lazy('ssid_list')



################################################
#
# Devices
#
###############################################

from django.views.generic import ListView, CreateView, UpdateView
from .models import ClientDevice, NetworkInfrastructureDevice
from .forms import ClientDeviceForm, NetworkInfrastructureDeviceForm
from django.urls import reverse_lazy

# ClientDevice views
class ClientDeviceListView(ListView):
    model = ClientDevice
    template_name = 'pages/device_list.html'

class ClientDeviceCreateView(CreateView):
    model = ClientDevice
    form_class = ClientDeviceForm
    template_name = 'pages/clientdevice_form.html'
    success_url = reverse_lazy('client_device_list')

class ClientDeviceUpdateView(UpdateView):
    model = ClientDevice
    form_class = ClientDeviceForm
    template_name = 'pages/clientdevice_form.html'
    success_url = reverse_lazy('client_device_list')

# NetworkInfrastructureDevice views
class NetworkInfrastructureDeviceListView(ListView):
    model = NetworkInfrastructureDevice
    template_name = 'device_list.html'

class NetworkInfrastructureDeviceCreateView(CreateView):
    model = NetworkInfrastructureDevice
    form_class = NetworkInfrastructureDeviceForm
    success_url = reverse_lazy('network_infrastructure_device_list')

class NetworkInfrastructureDeviceUpdateView(UpdateView):
    model = NetworkInfrastructureDevice
    form_class = NetworkInfrastructureDeviceForm
    success_url = reverse_lazy('network_infrastructure_device_list')


from django.views import View
from django.shortcuts import render

class GeneralDeviceListView(View):
    template_name = 'pages/device_list.html'

    def get(self, request, *args, **kwargs):
        client_devices = ClientDevice.objects.all()
        network_devices = NetworkInfrastructureDevice.objects.all()
        devices = list(client_devices) + list(network_devices)
        return render(request, self.template_name, {'devices': devices})
