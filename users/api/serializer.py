from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, ListSerializer,StringRelatedField

from users.models import Supplier,OurUser,Regular,BaseUers

class OurUserSerializer(ModelSerializer):
    class Meta:
        model = OurUser
        fields = "__all__"


class SupplierSerializer(ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"



