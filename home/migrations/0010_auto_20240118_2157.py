from django.db import migrations, models

def add_default_site(apps, schema_editor):
    Site = apps.get_model('home', 'Site')
    if not Site.objects.exists():
        Site.objects.create(name='Default Site', location='Default')

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_network_broadcast_ip_network_ip_range_and_more'),  # replace with your actual previous migration
    ]

    operations = [
        migrations.RunPython(add_default_site),
    ]
