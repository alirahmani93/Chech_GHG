from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as log_in, logout as log_out
from django.views.generic import UpdateView

from kavenegar import KavenegarAPI,APIException,HTTPException
from chech_GHG.settings import KAVENAGAR_API_KEY

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
























































def send_sms(request):
    try:
        api = KavenegarAPI(KAVENAGAR_API_KEY)
        # api = KavenegarAPI("654A326F39354853692B30347450356E4D65745659655230743164384A7546757A3964416B4C586C6647413D")
        params = {
            'sender': '',  # optional
            'receptor': '09195341154',  # multiple mobile number, split by comma
            'message': 'test mikonim',
        }
        response = api.sms_send(params)
        print(response)
        return HttpResponse("sms RAFT")
    except APIException as e:
        return HttpResponse(e)
    except HTTPException as e:
        return HttpResponse(e)


def call(request):
    try:
      api = KavenegarAPI(KAVENAGAR_API_KEY)
      params = {
        'receptor': '09195341154',
        'message': 'Hello'
      }
      response = api.call_maketts(params)
      print(response)
      return HttpResponse("call RAFT")

    except APIException as e:
        return HttpResponse(e)
    except HTTPException as e:
        return HttpResponse(e)


def verify(request):
    try:
        api = KavenegarAPI(KAVENAGAR_API_KEY)
        params = {
            'receptor': '09195341154',
            'template': '',
            'token': 'verify',
            'token2': 'verify2',
            'token3': 'verify3',
            'type': 'sms',  # sms vs call
        }
        response = api.verify_lookup(params)
        print(response)
        return HttpResponse("verify RAFT")

    except APIException as e:
        return HttpResponse(e)
    except HTTPException as e:
        return HttpResponse(e)
