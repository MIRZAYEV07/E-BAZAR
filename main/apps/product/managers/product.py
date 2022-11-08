

from main.apps.common.managers import BaseManager

class ProductManager(BaseManager):

    def retrieve_products_in_sale(self):

        qs = self.filter(is_sale=True)
        return qs

    

