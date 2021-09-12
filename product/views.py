from datetime import datetime
from json import loads, dumps

from django.db.models import Q , Count
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View, DetailView, FormView

from .models import Product, Brand, Category, Media
from .form import ProductForm


# Create your views here.
class ProductList(ListView):
    context_object_name = 'list_p'
    template_name = 'shop.html'
    queryset = Product.objects.all()
    model = Product


class ProductDetails(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = "p_details"


class ProductFormView(FormView):
    template_name = "producr_form.html"
    form_class = ProductForm
    success_url = "Thank YOU"

class TestAnnotated(ListView):
    template_name = "producr_form.html"
    model = Product
    context_object_name = "p_list"
    queryset = Product.objects.all()
    # queryset = Product.objects.annotate(status_type=Count("cat"))

def show_all_product(request, cat):
    # obj = list(Product.objects.all().order_by("id").values())
    # return JsonResponse(obj, safe=False)

    # list_product = Product.objects.filter(cat=Category.objects.get(title=cat).values("id")).values()
    list_product = list(Product.objects.filter(cat__title__contains=cat).values())
    print(list_product)
    context = {
        "title": "Product List",
        "list_p": list_product,
        "request_time": datetime.strptime("26/08/2021", "%d/%m/%Y"),
    }

    print("context", context)
    # return JsonResponse(list_product, safe=False)
    return render(request, "shop.html", context)


def show_all_brand(request):
    obj = list(Brand.objects.all().order_by("id").values())
    return JsonResponse(obj, safe=False)


def show_all_category(request):
    obj = list(Category.objects.all().order_by("id").values())
    return JsonResponse(obj, safe=False)


def show_all_media(request):
    obj = Media.objects.all().order_by("image_product_id").values()
    media_list = []
    for elm in obj:
        print(elm)
        media_list.append({
            "picture": obj.picture,
            "image_product": obj.image_product,
            "discription": obj.discription,
            "video_description": obj.video_description,
            "slug": obj.slug,
        })
    return JsonResponse(media_list, safe=False)


def selected_product(request, id):
    # uuid = str(uuid)
    # print(uuid)
    obj = Product.objects.filter(id=id).values()
    attribute = []
    for attr in obj:
        attribute.append({
            "Product": attr.name,
            "Brand": attr.brand,
            "Count": attr.count,
        })
    # return render(request, "app1/show_Questions.html", context)
    return JsonResponse(attribute, safe=True)
