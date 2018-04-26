# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import logout as logout
import json
from datetime import date, time, datetime, timedelta


from . nakljucje import *

#tu naj bi se prijavil z authenticate
from django.contrib.auth import authenticate, login



# Create your views here.



#domače strani v slo in ing
#ko se odpre preveri ce so jeziki sole in avatarji prazni



def napoved_indeks(request):
    context={}
    context["n"]=13
    return render(request,"napoved_indeks.html",context)