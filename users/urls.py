
from django.urls import path
from rest_framework.routers import SimpleRouter

from .api.api_view import *
from .views import register, login, logout, UpdateProfile, send_sms, verify, call

###

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('<pk>/update', UpdateProfile.as_view(), name="UpdateUsernameFiled"),

    path("sms/", send_sms,name="send_sms"),
    path("call/", call,name="call"),

    path("vaerify/", verify,name="verify"),

]
