from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # You can add more fields as needed

    def __str__(self):
        return self.name

class NETWORK(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    vlan_id = models.IntegerField()
    network_color = models.CharField(max_length=7, help_text="Enter the color in HEX format (e.g., #FF5733)")
    gateway = models.GenericIPAddressField(help_text="Enter the gateway IP address")
    dhcp_range = models.CharField(max_length=50, help_text="Enter the DHCP range (e.g., 192.168.1.100-192.168.1.200)")

    def __str__(self):
        return f"{self.name} (NETWORK {self.vlan_id})"

    class Meta:
        unique_together = ('site', 'vlan_id')

class SSID(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    ssid_name = models.CharField(max_length=100)
    network = models.ForeignKey(NETWORK, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ssid_name}"

class PatchPanel(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number_of_ports = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class PatchPanelPort(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
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

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    network = models.ForeignKey(NETWORK, on_delete=models.CASCADE)
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

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    network = models.ForeignKey(NETWORK, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=INFRASTRUCTURE_TYPES)
    number_of_ports = models.IntegerField(help_text="Number of ports (for switches and routers)")

    def __str__(self):
        return f"{self.name} - {self.type}"

class Port(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    device = models.ForeignKey(NetworkInfrastructureDevice, related_name='ports', on_delete=models.CASCADE)
    port_number = models.IntegerField()
    active_networks = models.ManyToManyField(NETWORK, blank=True)
    is_trunk = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.device.site.name} - Port {self.port_number} on {self.device.name}"


#Serviços disponibilizados por cada equipamento
# Listagem dos tabelas com ordenação por campo.
