from datetime import datetime
from json import loads, dumps
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product, Brand, Category, Media


# Create your views here.

def show_all_product(request, cat):
    # obj = list(Product.objects.all().order_by("id").values())
    # return JsonResponse(obj, safe=False)

    # list_product = Product.objects.filter(cat=Category.objects.get(title=cat).values("id")).values()
    list_product = Category.objects.filter(title=cat)
    print( list_product)
    context = {
        "title": "Product List",
        "list_p": list_product,
        "request_time": datetime.strptime("26/08/2021", "%d/%m/%Y"),
    }
    render(request, "list_p.html", context,status=205)


def show_all_brand(request):
    obj = list(Brand.objects.all().order_by("id").values())
    return JsonResponse(obj, safe=False)


def show_all_category(request):
    obj = list(Category.objects.all().order_by("id").values())
    return HttpResponse(obj)


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


def selcted_product(request, id):
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


def show_price(request, upc):
    obj = Product.objects.filter(upc__exact=upc).values()
    print(obj, upc)
    if (datetime.time > obj.date_start) and (datetime.time < obj.date_end):
        object.cost = obj.Temporary_price
        return obj.cost
    else:
        obj.cost = obj.price
        return obj.cost
