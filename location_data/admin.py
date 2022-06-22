from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import LocationData


class Admin(ModelAdmin):
    geomap_field_latitude = "id_latitude"
    geomap_field_longitude = "id_longitude"


admin.site.register(LocationData, ModelAdmin)
