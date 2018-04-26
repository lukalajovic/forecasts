from django.conf.urls import include, url
from forecasting.views import *

urlpatterns = [


    url(r'^napoved_index/', napoved_indeks, name='napovedtestvsega2'),
]

"""
url(r'^glavna', glavna_stran,name='glavna_stran'),

#url(r'^podatki', podatki, name='podatki'),

url(r'^test', test, name='test'),
url(r'^preizkus', test2, name='preizkus'),


url(r'^pravi_prikazX/', prikazX, name='prikazX'),
url(r'^prikaz/(?P<n>\d+)', glavna_stran2, name='prikaz'),
url(r'^nakljucni_podatki/(?P<n>\d+)', nakljucni_podatki, name='nakljucni_podatki'),
url(r'^nakljucen_prikaz/', nakljucen_prikaz, name='nakljucen_prikaz'),
url(r'^napoved_test/(?P<n>\d+)', napoved_test, name='napovedtest'),
url(r'^napoved_test/', napoved_test, name='napovedtest2'),
url(r'^napoved_test_vse/(?P<n>\d+)', napoved_test_vse, name='napovedtestvse'),
url(r'^napoved_test_vse/', napoved_test_vse, name='napovedtestvse2'),
url(r'^napoved_vsega/', napoved_vsega, name='napovedtestvsega2'),
"""