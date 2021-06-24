from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties,Incidences
import requests
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'

def county_datasets(request):
	counties = serialize('geojson', Counties.objects.all())
	return HttpResponse(counties,content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')
# def iqair_api(request):
# 	responce = requests.get(https://api.airvisual.com/v2/city?city={{Counties}}&state=punjab&country=Pakistan&key=eaae2370-f8eb-4194-9204-609377b4e207)
# 	data= responce.loadjson
#   return data.json