from django.urls import path

from .views import RegisterView, LoginView, ProfileUpdateView, sign_up, password_change_done, \
    password_change, search

from django.contrib.auth import views as authViews
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
    # path('<pk>/update', UpdateProfile.as_view(), name="UpdateUsernameFiled")

]
