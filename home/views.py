from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, View, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


# Helper function to get the current site
def get_current_site(request):
    site_id = request.session.get('current_site_id', None)
    if site_id:
        return get_object_or_404(Site, id=site_id)
    else:
        default_site = Site.objects.first()  # get the first available site
        request.session['current_site_id'] = default_site.id
        return default_site

# View to set the current site
def set_current_site(request):
    site_id = request.GET.get('site_id')
    if site_id:
        request.session['current_site_id'] = int(site_id)
    return redirect('index')

# Index view
def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

# NETWORK views
class NETWORKListView(ListView):
    model = NETWORK
    template_name = 'pages/network_list.html'
    context_object_name = 'networks'

    def get_queryset(self):
        current_site = get_current_site(self.request)
        query = self.request.GET.get('q')
        if query:
            return NETWORK.objects.filter(site=current_site, name__icontains=query)
        return NETWORK.objects.filter(site=current_site)

class NETWORKCreateView(CreateView):
    model = NETWORK
    form_class = NETWORKForm
    template_name = 'pages/network_form.html'
    success_url = reverse_lazy('network_list')

    def form_valid(self, form):
        form.instance.site = get_current_site(self.request)
        return super(NETWORKCreateView, self).form_valid(form)
    
    def form_invalid(self, form):
        # Log form errors for debugging
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['site'] = get_current_site(self.request).pk
        return initial

class NETWORKUpdateView(UpdateView):
    model = NETWORK
    form_class = NETWORKForm
    template_name = 'pages/network_form.html'
    success_url = reverse_lazy('network_list')

class NETWORKDeleteView(DeleteView):
    model = NETWORK
    template_name = 'pages/network_confirm_delete.html'  # Create a template for delete confirmation
    success_url = reverse_lazy('network_list')  # URL to redirect after successful deletion

# SSID views
class SSIDListView(ListView):
    model = SSID
    template_name = 'pages/ssid_list.html'
    context_object_name = 'ssids'

    def get_queryset(self):
        current_site = get_current_site(self.request)
        return SSID.objects.filter(site=current_site)

class SSIDCreateView(CreateView):
    model = SSID
    form_class = SSIDForm
    template_name = 'pages/ssid_form.html'
    success_url = reverse_lazy('ssid_list')

    def form_valid(self, form):
        form.instance.site = get_current_site(self.request)
        return super().form_valid(form)

class SSIDUpdateView(UpdateView):
    model = SSID
    form_class = SSIDForm
    template_name = 'pages/ssid_form.html'
    success_url = reverse_lazy('ssid_list')

# ClientDevice views
class ClientDeviceListView(ListView):
    model = ClientDevice
    template_name = 'pages/device_list.html'

    def get_queryset(self):
        current_site = get_current_site(self.request)
        return ClientDevice.objects.filter(site=current_site)

class ClientDeviceCreateView(CreateView):
    model = ClientDevice
    form_class = ClientDeviceForm
    template_name = 'pages/clientdevice_form.html'
    success_url = reverse_lazy('client_device_list')

    def form_valid(self, form):
        form.instance.site = get_current_site(self.request)
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super(ClientDeviceCreateView, self).get_form(form_class)
        current_site = get_current_site(self.request)
        form.fields['network'].queryset = NETWORK.objects.filter(site=current_site)
        return form

class ClientDeviceUpdateView(UpdateView):
    model = ClientDevice
    form_class = ClientDeviceForm
    template_name = 'pages/clientdevice_form.html'
    success_url = reverse_lazy('client_device_list')

    def get_form(self, form_class=None):
        form = super(ClientDeviceUpdateView, self).get_form(form_class)
        current_site = get_current_site(self.request)
        form.fields['network'].queryset = NETWORK.objects.filter(site=current_site)
        return form

# NetworkInfrastructureDevice views
class NetworkInfrastructureDeviceListView(ListView):
    model = NetworkInfrastructureDevice
    template_name = 'pages/device_list.html'

    def get_queryset(self):
        current_site = get_current_site(self.request)
        return NetworkInfrastructureDevice.objects.filter(site=current_site)

class NetworkInfrastructureDeviceCreateView(CreateView):
    model = NetworkInfrastructureDevice
    form_class = NetworkInfrastructureDeviceForm
    success_url = reverse_lazy('network_infrastructure_device_list')

    def form_valid(self, form):
        form.instance.site = get_current_site(self.request)
        return super().form_valid(form)

class NetworkInfrastructureDeviceUpdateView(UpdateView):
    model = NetworkInfrastructureDevice
    form_class = NetworkInfrastructureDeviceForm
    success_url = reverse_lazy('network_infrastructure_device_list')

# GeneralDeviceListView
class GeneralDeviceListView(View):
    template_name = 'pages/device_list.html'

    def get(self, request, *args, **kwargs):
        current_site = get_current_site(request)
        client_devices = ClientDevice.objects.filter(site=current_site)
        network_devices = NetworkInfrastructureDevice.objects.filter(site=current_site)
        devices = list(client_devices) + list(network_devices)
        context = {'devices': devices}
        return render(request, self.template_name, context)

