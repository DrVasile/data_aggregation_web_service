from django.db import models
from django_admin_geomap import GeoItem


class LocationData(models.Model, GeoItem):

    object_id = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    @property
    def geomap_longitude(self):
        return str(self.longitude)
