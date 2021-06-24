from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

# class Migration(migrations.Migration):
#
#     operations = [
#         CreateExtension('postgis'),
#         ...
#     ]

# Create your models here.
class Incidences(models.Model):
	name = models.CharField(max_length=20)
	location = models.PointField(srid=4326)
	objects = GeoManager()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural =" Incidences"


class Counties(models.Model):
	province = models.CharField(max_length=254)
	province_c = models.FloatField()
	district = models.CharField(max_length=254)
	district_c = models.IntegerField()
	remarks = models.CharField(max_length=254)
	m_20110324 = models.IntegerField()
	d_name = models.CharField(max_length=254)
	geom = models.MultiPolygonField(srid=4326)


	def __unicode__(self):

		return self.d_name

	class Meta:
		verbose_name_plural = 'Counties'


