# forms.py

from django import forms
from .models import *
from django.forms import Select

class NETWORKSelectWidget(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if isinstance(label, NETWORK):
            option['label'] = label.name  # Display only the NETWORK name
        return option

class NETWORKForm(forms.ModelForm):
    class Meta:
        model = NETWORK
        fields = ['site', 'name', 'vlan_id', 'network_color', 'gateway', 'netmask', 'dhcp_server', 'dhcp_start', 'dhcp_end', 'primary_dns', 'secondary_dns']
        widgets = {
            'network_color': forms.TextInput(attrs={'type': 'color'}),
            'site': forms.HiddenInput(),  # Set the 'site' field as hidden
            'netmask': forms.Select(),  # Use a standard select widget for the netmask
            'dhcp_server': forms.Select(choices=[(True, 'Yes'), (False, 'No')]),  # Dropdown for DHCP Server (Yes/No)
        }
        
    def __init__(self, *args, **kwargs):
        super(NETWORKForm, self).__init__(*args, **kwargs)
        self.fields['dhcp_server'].initial = False

class SSIDForm(forms.ModelForm):
    class Meta:
        model = SSID
        fields = ['site', 'ssid_name', 'network']

class ClientDeviceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        site = kwargs.pop('site', None)
        super(ClientDeviceForm, self).__init__(*args, **kwargs)
        if site:
            self.fields['network'].queryset = NETWORK.objects.filter(site=site)
        self.fields['network'].widget = NETWORKSelectWidget()  # Set the custom widget

    class Meta:
        model = ClientDevice
        fields = '__all__'

class NetworkInfrastructureDeviceForm(forms.ModelForm):
    class Meta:
        model = NetworkInfrastructureDevice
        fields = '__all__'