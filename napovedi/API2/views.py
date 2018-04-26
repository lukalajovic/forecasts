
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse

import json


from . health import  *
# Create your views here.

"""
def poljubni2(request):
    T="DT"
    data=izpisi(T)
    return JsonResponse(data, safe=False)

def poljubni(request,Tr="DT"):

    if len(Tr.split('qqq'))==1:
        Tr=str(Tr)
        if Tr=="BMI":
            data=izpisi_bmi("")
        else:
            data = izpisi(Tr)
    else:
        G=Tr.split('qqq')
        if G[0]=="BMI":
            print("novgorod"+G[1])
            data=izpisi_bmi(G[1])
        else:
            data=izpisi(G[0],G[1])
    Tr=str(Tr)

    #data=izpisi(Tr)

    return JsonResponse(data, safe=False)

def vse(request, identiteta=""):
    data=izpisi_vse(identiteta)
    return JsonResponse(data, safe=False)
"""

def indeks(request,indeks="DT"):
    if len(indeks.split('qqq'))==1:
        indeks=str(indeks)
        if indeks=="BMI":
            data=izpisi_bmi("")
        else:
            data = izpisi(indeks)
    else:
        G=indeks.split('qqq')
        if G[0]=="BMI":

            data=izpisi_bmi(G[1])
        else:
            data=izpisi(G[0],G[1])
    indeks=str(indeks)
    return JsonResponse(data, safe=False)

def indeks_risk(request,indeks="1900"):
    ind=str(indeks)
    data=risk_index(ind)
    return JsonResponse(data, safe=False)