# Generated by Django 4.2.7 on 2024-01-17 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_clientdevice_site_networkinfrastructuredevice_site_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdevice',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.site'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='networkinfrastructuredevice',
            name='site',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='home.site'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patchpanel',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.site'),
        ),
        migrations.AlterField(
            model_name='patchpanelport',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.site'),
        ),
        migrations.AlterField(
            model_name='port',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.site'),
        ),
        migrations.AlterField(
            model_name='ssid',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.site'),
        ),
        migrations.AlterField(
            model_name='vlan',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.site'),
        ),
    ]