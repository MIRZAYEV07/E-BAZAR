from rest_framework import serializers
from ..models.product import ProductModel
from main.apps.category.models import Category
from ...account.serializers.user import UserSerializer
from ..serializers.sub_features import SubFeatureValueListSerializer
from ...category.serializers import CategoryCreateSerializer
from ..serializers.comments import CommentCreateSerializer


class ProductCreateSerializers(serializers.ModelSerializer):


    class Meta:
        model = ProductModel
        fields = (
            'title',
            'definition',
            'owner',
            'category',
            'main_features',
            'sub_features',
            'pictures',
            'ratings',
            'price_without_sale',
            'price_in_sale',
            'currency',
            'is_sale',
            'is_credit_for',


        )


class ProductListSerializers(serializers.ModelSerializer):

    category = CategoryCreateSerializer()
    owner = UserSerializer()
    sub_features = SubFeatureValueListSerializer()
    comments = CommentCreateSerializer()

    class Meta:
        model = ProductModel
        fields = (
            'title',
            'definition',
            'owner',
            'category',
            'main_features',
            'sub_features',
            'pictures',
            'ratings',
            'price_without_sale',
            'price_in_sale',
            'currency',
            'is_sale',
            'is_credit_for',
            'comments',
        )

