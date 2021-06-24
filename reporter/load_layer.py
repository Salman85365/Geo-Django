import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

countie_mapping = {
    'province': 'PROVINCE',
    'province_c': 'PROVINCE_C',
    'district': 'DISTRICT',
    'district_c': 'DISTRICT_C',
    'remarks': 'Remarks',
    'm_20110324': 'M_20110324',
    'd_name': 'D_NAME',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data2/counties.shp'))

def run(verbose=True):
	lm = LayerMapping(Counties, county_shp, countie_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)