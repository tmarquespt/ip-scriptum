from django.db import models

class VLAN(models.Model):
    name = models.CharField(max_length=100)
    vlan_id = models.IntegerField(unique=True)
    vlan_color = models.CharField(max_length=7, help_text="Enter the color in HEX format (e.g., #FF5733)")
    gateway = models.GenericIPAddressField(help_text="Enter the gateway IP address")
    dhcp_range = models.CharField(max_length=50, help_text="Enter the DHCP range (e.g., 192.168.1.100-192.168.1.200)")

    def __str__(self):
        return f"{self.name} (VLAN {self.vlan_id})"

class SSID(models.Model):
    ssid_name = models.CharField(max_length=100)
    vlan = models.ForeignKey(VLAN, on_delete=models.CASCADE)

    def __str__(self):
        return self.ssid_name

class PatchPanel(models.Model):
    name = models.CharField(max_length=100)
    number_of_ports = models.IntegerField()

    def __str__(self):
        return self.name

class PatchPanelPort(models.Model):
    patch_panel = models.ForeignKey(PatchPanel, related_name='ports', on_delete=models.CASCADE)
    port_number = models.IntegerField()

    def __str__(self):
        return f"Port {self.port_number} on {self.patch_panel.name}"

class ClientDevice(models.Model):
    DEVICE_TYPES = [
        ('SERVER', 'Server'),
        ('PRINTER', 'Printer'),
        ('PC', 'PC'),
        ('CAMERA', 'Camera'),
        # Add other client device types as needed
    ]

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    vlan = models.ForeignKey(VLAN, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=DEVICE_TYPES)

    CONNECTION_TYPE_CHOICES = [
        ('WIRELESS', 'Wireless'),
        ('WIRED_PATCH', 'Wired to Patch Panel'),
        ('WIRED_SWITCH', 'Wired to Switch/Router'),
    ]
    connection_type = models.CharField(max_length=15, choices=CONNECTION_TYPE_CHOICES, null=True, blank=True)
    ssid = models.ForeignKey(SSID, on_delete=models.SET_NULL, null=True, blank=True)
    patch_panel_port = models.ForeignKey(PatchPanelPort, on_delete=models.SET_NULL, null=True, blank=True)
    switch_router_port = models.ForeignKey('Port', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.ip_address} - {self.get_type_display()}"

class NetworkInfrastructureDevice(models.Model):
    INFRASTRUCTURE_TYPES = [
        ('SWITCH', 'Switch'),
        ('ROUTER', 'Router'),
        ('ACCESS_POINT', 'Access Point'),
    ]

    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    vlan = models.ForeignKey(VLAN, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=INFRASTRUCTURE_TYPES)
    number_of_ports = models.IntegerField(help_text="Number of ports (for switches and routers)")

    def __str__(self):
        return f"{self.name} - {self.type}"

class Port(models.Model):
    device = models.ForeignKey(NetworkInfrastructureDevice, related_name='ports', on_delete=models.CASCADE)
    port_number = models.IntegerField()
    active_vlans = models.ManyToManyField(VLAN, blank=True)
    is_trunk = models.BooleanField(default=False)

    def __str__(self):
        return f"Port {self.port_number} on {self.device.name}"
