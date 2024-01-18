# In one of your Django app's templatetags folder (e.g., myapp/templatetags/custom_filters.py)
from django import template
import ipaddress

register = template.Library()

@register.filter(name='calculate_broadcast_ip')
def calculate_broadcast_ip(gateway, netmask):
    try:
        # Convert the gateway to an IPv4 network object
        gateway_network = ipaddress.IPv4Network(gateway, strict=False)
        # Calculate the broadcast address based on the network and netmask
        broadcast_ip = gateway_network.broadcast_address
        return str(broadcast_ip)
    except Exception as e:
        return str(e)
