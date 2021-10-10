from datetime import datetime
from json import loads, dumps
from django.apps import apps

from django.db.models import Q, Count
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, View, DetailView, FormView
from rest_framework.views import APIView

from cart.forms import AddToCartForm
from .models import Product, Brand, Category, Media, Attribute  # ,Cart #, CartItem
from .form import ProductForm


# Create your views here.

class ProductList(ListView):
    model = Product
    context_object_name = 'list_p'
    template_name = 'shop.html'
    queryset = Product.objects.all()


class BrandList(ListView):
    model = Brand
    context_object_name = 'brand'
    template_name = 'sidebar.html'
    queryset = Brand.objects.all().values()
    print("PPPPPPPPPPPPPPPPPPPPPPPPPPP",queryset.values())


class SideBar(ListView):
    model = Category
    context_object_name = 'side'
    template_name = 'sidebar.html'


class PriceBar(ListView):
    model = Product
    context_object_name = 'price'
    template_name = 'sidebar.html'

    @cache_page(60 * 1)
    def get_queryset(self):
        down = Product.objects.order_by("-cost").first()
        up = Product.objects.order_by("-cost").last()

        queryset = {
            "down": down,
            "up": up
        }
        return queryset


def product_detail(request, pk):
    queryset = Product.objects.filter(pk=pk)
    print(queryset)
    if queryset.exists():
        product = queryset.first()
        form = AddToCartForm({"product": product, "quantity":1})
        return render(request, "product.html", {"product": product, "form": form})
    raise Http404

class ProductDetails(DetailView):
    model = Product
    query_pk_and_slug = "pk"

    # queryset = Product.objects.filter(pk=pk)
    template_name = "product.html"
    context_object_name = "p_details"


class ProductFormView(FormView):
    template_name = "producr_form.html"
    form_class = ProductForm

    success_url = "Thank YOU"


# class TestAnnotated(ListView):
#     template_name = "producr_form.html"
#     context_object_name = "p_list"
#     queryset = Product.objects.all()
#     model = Product
#     # queryset = Product.objects.annotate(status_type=Count("cat"))


# def show_all_product(request, cat):
#     # obj = list(Product.objects.all().order_by("id").values())
#     # return JsonResponse(obj, safe=False)
#
#     # list_product = Product.objects.filter(cat=Category.objects.get(title=cat).values("id")).values()
#     list_product = list(Product.objects.filter(cat__title__contains=cat).values())
#     print(list_product)
#     context = {
#         "title": "Product List",
#         "list_p": list_product,
#         "request_time": datetime.strptime("26/08/2021", "%d/%m/%Y"),
#     }
#
#     print("context", context)
#     # return JsonResponse(list_product, safe=False)
#     return render(request, "shop.html", context)


def show_all(request, pmodel=None, pk=None):
    pmodel = str(pmodel).capitalize()
    app_models = apps.get_app_config(request.path.split("/")[1]).get_models()
    model_list = list()
    for model in app_models:
        if str(model.__name__) == pmodel:
            pmodel = model
            obj = pmodel.objects.all().order_by("id")
            obj2 = pmodel.objects.all().order_by("id")
            list_obj = list(pmodel.objects.all().order_by("id").values())
            context = {
                "obj_list": list_obj,
                "obj2": obj2
            }
            # Just Models
            if not pk:
                return render(request, "test.html", {"obj2": obj2, "list_obj": list_obj})
                # return JsonResponse(obj_list, safe=False)

            # object exist
            elif pk <= len(obj):
                obj_detail = list(obj.filter(id=pk).values())
                return render(request, "test.html", {"obj2": obj_detail})
                # return JsonResponse(obj_detail, safe=False)

            # object not exist
            elif pk > len(obj):
                return HttpResponse("chizi ba in ID mojood nist")
                # return render(request, "404.html", {})

        model_list.append(model.__name__)
    return render(request, "404.html", {"qs": model_list, "body": "مدل هایی که می توانید سرچ کنید"})
    # return JsonResponse({"Our_models_are": model_list}, safe=False)


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


class MediaView(ListView):
    model = Media
    template_name = "test.html"
    context_object_name = "medias"
    # queryset = Media.objects.all()
# queryset = Media.objects.all()


# class CommentSerializeView(APIView):
#     def putt(self, request):
#         product = get_object_or_404(Product,id)
#
#
#     def delete(self,id):
#         product = get_object_or_404(Product,id)
