from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView,Response,Request,Http404
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework import filters
from .serializer import ProductSerializer, CategorySerializer,BrandSerializer

from product.models import Product, Category, Brand


############## PAGINATION ##############


class CustomizePagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'


############## Product ##############

class ProductListView(ListCreateAPIView):
    pagination_class = CustomizePagination

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]



class ProductViewset(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            print("hereee")
            serializer = self.get_serializer(page, many=True)
            print("outtttt")

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewset(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandViewset(ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
