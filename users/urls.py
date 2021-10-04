
from django.urls import path
from rest_framework.routers import SimpleRouter

from .api.api_view import *
from .views import register, login, logout, UpdateProfile

###

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('<pk>/update', UpdateProfile.as_view(), name="UpdateUsernameFiled")

]
