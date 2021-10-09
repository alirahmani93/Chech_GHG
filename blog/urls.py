from django.shortcuts import render
from django.urls import path, include



def blog(request):
    # return render(request,"index.html",{})
    return render(request,"blog/index.html",{})

urlpatterns = [

    path('blog-ma', blog, name='blog'),
    # path('about/', about_us, name='about-us'),
    # path('contact/', contact_us, name='contact-us'),



    ]