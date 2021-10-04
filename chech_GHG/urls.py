import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from rest_framework import views
from .view import home, about_us, contact_us, send_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

    path('', home, name='home_page'),
    path('about/', about_us, name='about-us'),
    path('contact/', contact_us, name='contact-us'),
    path('email/', send_comment, name='email'),
    # path("auth-token-auth/",views.obtain)


    path('product/', include("product.urls"), name="prd"),
    path('account/', include("users.urls"), name="acc"),
    path('cart/', include("cart.urls"), name="cart"),
    path('payment/', include("payment.urls")),
    # path('shipping/', include("shipping.urls")),
    # path('wallet/', include("wallet.urls")),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
