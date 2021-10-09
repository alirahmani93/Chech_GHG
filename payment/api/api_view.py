from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView,Response,Request,Http404
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework import filters
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated

from .serializer import PaymentSerializer
# from payment.models import Invoice

class PaymentSerializerView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PaymentSerializer
    pagination_class = PageNumberPagination
    # queryset = Invoice.objects.all()


class PaymentViewset(ReadOnlyModelViewSet):
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated]
    # queryset = Invoice.objects.all()
    serializer_class = PaymentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
