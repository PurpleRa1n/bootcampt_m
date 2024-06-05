from django.contrib.gis.db import models as gis_models
from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=120)
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=10)


class ServiceArea(models.Model):
    name = models.CharField(max_length=80)
    price = models.FloatField()
    geojson = gis_models.PolygonField()
    provider = models.ForeignKey(Provider, related_name='service_areas', on_delete=models.CASCADE)
