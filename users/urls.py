from django.urls import path

from .views import RegisterView, LoginView, LogOut

###

urlpatterns = [
    # path('login/', login, name='login'),
    path('register/', RegisterView.as_view, name='register'),
    path('login/', LoginView.as_view, name='login'),
    path('logout/', LogOut.as_view, name='logout'),
    # path('logout/', logout, name='logout'),

]
