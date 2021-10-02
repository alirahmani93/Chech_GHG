from rest_framework import serializers

from product.models import Product

#
# class ProductSerializer(serializers.Serializer):
#     prodcut_id = serializers.PrimaryKeyRelatedField(many=True)
#
#     def create(self, validated_data):
#         pr_id = int(self.context.get("product_id"))
#         return Product.objects.create(pr_id=pr_id, **validated_data)
#
#     def update(self, instance, validated_data):
#         instance
#
#         pass
