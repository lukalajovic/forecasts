from django.conf.urls import include, url
from API2.views import *
#(?P<id>\d+)
urlpatterns = [
    #url(r'^poljubno/(?P<n>\d+)',poljubni,name="poljubno"),
    #url(r'^poljubno/', poljubni, name="poljubno2"),
    #url(r'^poljubno/(?P<Tr>[\w ]+)',poljubni,name="poljubno"),
    #url(r'^poljubno/(?P<indeks>.*)', indeks, name="poljubno"),
    #url(r'^vse/', vse, name="vse"),
    url(r'^index/(?P<indeks>.*)', indeks, name="poljubno"),
    url(r'^risk/(?P<indeks>.*)', indeks_risk, name="poljubno"),
]