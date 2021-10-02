from django.urls import path

from .views import *

urlpatterns = [
    path('product-list/',                   cache_page(60)(ProductList.as_view()),      name="shop"),
    path('product-details/<int:pk>',        ProductDetails.as_view(),   name="product-details"),

    path('show_all/<str:pmodel>/',          show_all,                   name="show_all_list"),
    path('show_all/<str:pmodel>/<int:pk>',  show_all,                   name="show_all"),

    path('selcted_p/<int:id>',              selected_product,           name="selected_product"),
    path('form/',                           ProductFormView.as_view(),  name="ProdfuctForm"),
    path('annotated/',                      TestAnnotated.as_view(),    name="annotated"),
    path('annotated/',                      TestAnnotated.as_view(),    name="annotated"),
    # path('test/',                           Media.as_view(),            name="annotated"),
    path('sidebar/',                        SideBar.as_view(),          name="sidebar"),
    path('sidebar/',                        BrandList.as_view(),        name="sidebar"),

    path('media/',                        MediaView.as_view(),        name="media_view"),

]

# path('show_all_p/<str:cat>', show_all_product, name="show_all_product"),
