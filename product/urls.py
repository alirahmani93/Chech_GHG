from django.urls import path

from .views import *

urlpatterns = [
    path('product-list/', ProductList.as_view(), name="shop"),
    path('product-details/<int:pk>', ProductDetails.as_view(), name="product-details"),
    path('show_all_b/', show_all_brand, name="show_all_brand"),
    path('show_all_c/', show_all_category, name="show_all_category"),
    path('show_all_m/', show_all_media, name="show_all_media"),
    path('selcted_p/<int:id>', selected_product, name="selected_product"),
]

# path('show_all_p/<str:cat>', show_all_product, name="show_all_product"),
