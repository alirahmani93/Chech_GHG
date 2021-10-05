from django.urls import path
from django.contrib.auth import views as authViews

from .views import *

###

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page': 'index'}, name='logout'),
    path('changepassword/', password_change, name='change_password'),
    path('changepassword/done', password_change_done, name='change_password_done'),

    # path('login/', login, name='login'),
    # path('register/', register, name='register'),
    # path('logout/', logout, name='logout'),
    # path('<pk>/update', UpdateProfile.as_view(), name="UpdateUsernameFiled"),

    path("sms/", send_sms, name="send_sms"),
    path("call/", call, name="call"),

    path("vaerify/", verify, name="verify"),

]
