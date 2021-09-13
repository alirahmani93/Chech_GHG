from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as log_in, logout as log_out
from django.views.generic import UpdateView

from .models import OurUser, Regular, Staff, Supplier


def login(request):
    if request.method == "GET":
        return render(request, "login-register.html", {})

    elif request.method == "POST":
        email = request.POST.get("email", None)
        if not email:
            return render(request, "404.html", {})

        password = request.POST.get("password", None)
        if not password:
            return render(request, "404.html", {})

        user = authenticate(username=email, password=password)
        if user:
            log_in(request, user)
            return HttpResponse("خوش آمدید")
        else:
            return HttpResponse("ورود موفقیت آمیز نبود")

    return render(request, "login-register.html", {})


def logout(request):
    pass


def register(request):
    pass



class UpdateProfile(UpdateView):    #(LoginRequiredMixin, UpdateView):
    model = OurUser
    template_name = "test.html"
    fields = ["username"]
    success_url = "/"

