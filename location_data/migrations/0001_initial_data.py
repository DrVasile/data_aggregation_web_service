# Generated by Django 3.2.13 on 2022-06-23 22:49

from django.db import migrations, models
import django_admin_geomap


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="LocationData",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ("object_id", models.CharField(max_length=128)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
            bases=(models.Model, django_admin_geomap.GeoItem),
        ),
    ]
