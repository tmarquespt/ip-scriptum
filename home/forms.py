# forms.py

from django import forms
from .models import *

class VLANForm(forms.ModelForm):
    class Meta:
        model = VLAN
        fields = ['site', 'name', 'vlan_id', 'vlan_color', 'gateway', 'dhcp_range']
        widgets = {
            'vlan_color': forms.TextInput(attrs={'type': 'color'}),
            # Add other widgets as needed
        }

class SSIDForm(forms.ModelForm):
    class Meta:
        model = SSID
        fields = ['site', 'ssid_name', 'vlan']

class ClientDeviceForm(forms.ModelForm):
    class Meta:
        model = ClientDevice
        fields = '__all__'

class NetworkInfrastructureDeviceForm(forms.ModelForm):
    class Meta:
        model = NetworkInfrastructureDevice
        fields = '__all__'