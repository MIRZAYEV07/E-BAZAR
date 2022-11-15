from rest_framework import serializers

from .models import CartModel,TotalCartModel

class CartSerializer(serializers.ModelSerializer):

    class Meta:

        model = CartModel
        fields = "__all__"

class TotalCartSerializer(serializers.ModelSerializer):

    class Meta:

        model = TotalCartModel
        fields = "__all__"