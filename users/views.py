from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import resolve
from django.views.decorators.http import require_POST
from django.views.generic import FormView, UpdateView, DetailView

from users.forms import RegistrationForm, LoginForm, SignupForm, ChangePasswordForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as log_in, logout as log_out, get_user_model, \
    update_session_auth_hash
from django.views.generic import UpdateView, FormView
from django.template import loader
from users.forms import RegistrationForm, LoginForm, SignupForm, ChangePasswordForm

from chech_GHG.settings import KAVENAGAR_API_KEY
from .models import OurUser, Regular, Staff, Supplier
from kavenegar import KavenegarAPI, APIException, HTTPException
from chech_GHG.settings import KAVENAGAR_API_KEY

User = get_user_model()


#   #   #      #   #   #      #   #   #  register first method: class base  #   #   ##   #   ###   #   #   #   #
class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = 'home_page'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def login(request):
    if request.method == "GET":
        return render(request, "login-register.html", {})


#   #   #      #   #   #      #   #   #  register first method: class base  #   #   ##   #   ###   #   #   #   #
class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = 'home_page'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


#   #   #   # #   #   #       #  #   register second method: function base #   #   ##   #   ##   #   #
# @require_POST
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)


@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('change_password_done')
    else:
        form = ChangePasswordForm(instance=user)

    context = {
        'form': form,
    }


@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('change_password_done')
    else:
        form = ChangePasswordForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'change_password.html', context)


def password_change_done(request):
    return render(request, 'change_password_done.html')


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = 'home_page'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = User
    fields = ('username', 'avatar', 'email', 'phone')
    template_name = 'profile.html'
    success_url = 'home_page'

    def get_object(self, queryset=None):
        return self.request.user


# function base
@login_required
def search(request):
    query = request.GET.get("q")
    context = {}

    if query:
        users = User.objects.filter(username__icontains=query)

        # Pagination
        paginator = Paginator(users, 7)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
        }

    template = loader.get_template('search.html')

    return HttpResponse(template.render(context, request))


# class UpdateProfile(UpdateView):    #(LoginRequiredMixin, UpdateView):
#     model = OurUser
#     template_name = "test.html"
#     fields = ["username"]
#     success_url = "/"

def send_sms(request):
    try:
        api = KavenegarAPI(KAVENAGAR_API_KEY)
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
