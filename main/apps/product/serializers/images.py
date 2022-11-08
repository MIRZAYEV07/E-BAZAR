from rest_framework import serializers
from ..models.images import ProductImage

class ProductImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

