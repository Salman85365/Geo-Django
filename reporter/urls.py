from django.conf.urls import include,url

from .views import HomePageView, county_datasets,point_datasets,TempPageView,MoisturePageView,aqi_usPageView,aqi_cnPageView,IncidencesPageView
from django.conf.urls.static import static
from agricom import settings
urlpatterns = [
	url(r'^$', HomePageView.as_view(), name ='index'),
	url(r'^county_data/$', county_datasets, name = 'county'),
	url(r'^Temp/$', TempPageView.as_view(), name = 'Temp'),
	url(r'^Moisture/$',MoisturePageView.as_view(), name ='Moisture'),
	url(r'^aqi_us/$', aqi_usPageView.as_view(), name = 'aqi_us'),
	url(r'^aqi_cn/$', aqi_cnPageView.as_view(), name = 'aqi_cn'),
	url(r'^Incidences/$', IncidencesPageView.as_view(), name = 'Incidences'),
	url(r'^incidence_data/$', point_datasets, name = 'incidences'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)