from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer,HyperlinkedIdentityField,\
    ListSerializer,StringRelatedField


# from payment.models import Invoice



class PaymentSerializer(ModelSerializer):
    # invoice = StringRelatedField()

    class Meta:
        # model = Invoice
        fields = "__all__",

