import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

    # path('', home, name='home_page'),
    path('product/', include("product.urls")),
    path('account/', include("users.urls")),
    # path('cart/', include("cart.urls")),
    # path('shipping/', include("shipping.urls")),
    # path('payment/', include("payment.urls")),
    # path('wallet/', include("wallet.urls")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
