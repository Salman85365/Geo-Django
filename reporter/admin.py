from django.contrib import admin
from .models import Incidences, Counties
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
	pass
	list_display =('name','location')

class CountiesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('district','district_c')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
