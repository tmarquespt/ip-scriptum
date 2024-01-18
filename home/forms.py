# forms.py

from django import forms
from .models import *
from django.forms import Select

class VLANSelectWidget(Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super(VLANSelectWidget, self).create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if isinstance(label, VLAN):
            option['label'] = label.name  # Display only the VLAN name
        return option

class VLANForm(forms.ModelForm):
    class Meta:
        model = VLAN
        fields = ['site', 'name', 'vlan_id', 'vlan_color', 'gateway', 'dhcp_range']
        widgets = {
            'vlan_color': forms.TextInput(attrs={'type': 'color'}),
            'site': forms.HiddenInput(),  # Set the 'site' field as hidden
        }

class SSIDForm(forms.ModelForm):
    class Meta:
        model = SSID
        fields = ['site', 'ssid_name', 'vlan']

class ClientDeviceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        site = kwargs.pop('site', None)
        super(ClientDeviceForm, self).__init__(*args, **kwargs)
        if site:
            self.fields['vlan'].queryset = VLAN.objects.filter(site=site)
        self.fields['vlan'].widget = VLANSelectWidget()  # Set the custom widget

    class Meta:
        model = ClientDevice
        fields = '__all__'

class NetworkInfrastructureDeviceForm(forms.ModelForm):
    class Meta:
        model = NetworkInfrastructureDevice
        fields = '__all__'