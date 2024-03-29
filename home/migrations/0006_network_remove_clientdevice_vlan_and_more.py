# Generated by Django 4.2.7 on 2024-01-18 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_vlan_vlan_id_alter_vlan_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='NETWORK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('network_id', models.IntegerField()),
                ('network_color', models.CharField(help_text='Enter the color in HEX format (e.g., #FF5733)', max_length=7)),
                ('gateway', models.GenericIPAddressField(help_text='Enter the gateway IP address')),
                ('dhcp_range', models.CharField(help_text='Enter the DHCP range (e.g., 192.168.1.100-192.168.1.200)', max_length=50)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.site')),
            ],
            options={
                'unique_together': {('site', 'network_id')},
            },
        ),
        migrations.RemoveField(
            model_name='clientdevice',
            name='vlan',
        ),
        migrations.RemoveField(
            model_name='networkinfrastructuredevice',
            name='vlan',
        ),
        migrations.RemoveField(
            model_name='port',
            name='active_vlans',
        ),
        migrations.RemoveField(
            model_name='ssid',
            name='vlan',
        ),
        migrations.DeleteModel(
            name='VLAN',
        ),
        migrations.AddField(
            model_name='clientdevice',
            name='network',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.network'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='networkinfrastructuredevice',
            name='network',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.network'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='port',
            name='active_networks',
            field=models.ManyToManyField(blank=True, to='home.network'),
        ),
        migrations.AddField(
            model_name='ssid',
            name='network',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.network'),
            preserve_default=False,
        ),
    ]
