from ..common.managers import BaseManager
from .utils import generate_random_string


class OrderManager(BaseManager):
    def create_order_instance(self, user, data):

        from ..cart.models import TotalCartModel
        from .models import PAYMENTTypeChoices

        is_paid = False
        is_completed = False
        price = data.get("cart").total_price
        payment_type = data.get("payment_type")
        quantity = data.get("quantity", 1)



        if payment_type == PAYMENTTypeChoices.ONLINE:
            is_paid = True
            is_completed = True
            user.create_balance(-price)



        return self.create(
            owner=user,
            total_price=price,
            is_paid=is_paid,
            is_completed=is_completed,
            order_number=generate_random_string(),
            **data
        )
