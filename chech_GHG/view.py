from datetime import datetime
from json import loads, dumps
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View


# Create your views here.
def home(request):
    return render(request, "index.html", {'title': "home"})
