from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .api.api_view import ProductViewset, CategoryViewset,BrandViewset
from .views import *

simple_router = SimpleRouter()
simple_router.register("product", ProductViewset, basename="product")
simple_router.register("cat", CategoryViewset, basename="category")
simple_router.register("brand",BrandViewset , basename="brand")


urlpatterns = [
    path('product-list/',                   cache_page(1)(ProductList.as_view()),      name="shop"),
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

    path("api/",include(simple_router.urls)),

]
print(simple_router.urls)
# path('show_all_p/<str:cat>', show_all_product, name="show_all_product"),
