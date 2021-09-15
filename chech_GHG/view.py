from datetime import datetime
from json import loads, dumps
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from product.models import Category, Brand

# Create your views here.
from users.forms import LoginForm, RegistrationForm


def home(request):
    return render(request, "index.html", {'title': "home"})


def header(request, *args, **kwargs):
    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'header.html', context)


def footer(request, *args, **kwargs):
    context = {
        'login_form': LoginForm(request.POST or None),
        'register_form': RegistrationForm(request.POST or None)

    }
    return render(request, 'footer.html', context)
