from rest_framework import serializers

from ..cart.models import TotalCartModel
from .models import Order, PAYMENTTypeChoices




class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "guid",
            "cart",
            "payment_type",
            "order_number",
            "total_price",
            "quantity",
            "phone_number",
            "full_name",
        )




class OrderCreateSerializer(serializers.Serializer):
    book = serializers.SlugRelatedField(
        slug_field="guid",
        queryset=TotalCartModel.objects.all(),
    )

    payment_type = serializers.ChoiceField(choices=PAYMENTTypeChoices.choices)
    quantity = serializers.IntegerField(default=1)
    phone_number = serializers.CharField(required=False, max_length=15)
    full_name = serializers.CharField(required=False)

    def validate(self, attrs):
        self._errors = {}

        cart = attrs.get("cart")
        payment_type = attrs.get("payment_type")
        quantity = attrs.get("quantity", 1)
        user = self.context["request"].user



        if payment_type == PAYMENTTypeChoices.ONLINE:
            price = cart.total_price

            if price > user.check_balance:
                msg = "Insufficient balance"
                self._errors.update(
                    {
                        "errors": dict(
                            message=f"{msg}: {user.check_balance}",
                        ),
                    },
                )
        

        if self._errors:
            raise serializers.ValidationError(self._errors)

        return attrs


class CompleteOrderSerializer(serializers.Serializer):
    is_paid = serializers.BooleanField(default=False)
    is_completed = serializers.BooleanField(default=False)

    def update(self, instance, validated_data):
        instance.is_paid = validated_data.get("is_paid", instance.is_paid)
        instance.is_completed = validated_data.get(
            "is_completed",
            instance.is_completed,
        )
        instance.save()
        return validated_data
