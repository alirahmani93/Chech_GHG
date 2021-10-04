from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, ListSerializer,StringRelatedField

from product.models import Product, Brand, Category, Media, Attribute, Attributekey


class MediaSerializer(ListSerializer):
    class Meta:
        model = Media
        fields = "__all__"


class AtterkeySerializer(ModelSerializer):
    class Meta:
        model = Attributekey
        fields = "__all__"


class AttrSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Attributekey
        fields = "__all__"




class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        # extra_kwargs = {
        #     'view_name': 'category',
        #     "lookup_field":"cat"}


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(HyperlinkedModelSerializer):
    # media = MediaSerializer(many=True)
    # supplier = StringRelatedField()
    cat = CategorySerializer()
    brand = BrandSerializer()
    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ["supplier",]
        # exclude = ["supplier","cat"]
