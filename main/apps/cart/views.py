from rest_framework.generics import (ListCreateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)

from .models import CartModel,TotalCartModel
from .serializers import CartSerializer, TotalCartSerializer

class CartCreateView(ListCreateAPIView):

    queryset = CartModel.objects.all()
    serializer_class = CartSerializer


cart_create_view = CartCreateView.as_view()

class CartListView(ListAPIView):

    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

    search_fields = ["title"]

cart_list_view = CartListView.as_view()



class CartUpdateView(UpdateAPIView):

    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'slug'

cart_update_view = CartUpdateView.as_view()

class CartDeleteView(DestroyAPIView):

    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'slug'

cart_delete_view = CartDeleteView.as_view()

class TotalCartCreateView(ListCreateAPIView):

    queryset = TotalCartModel.objects.all()
    serializer_class = TotalCartSerializer


total_cart_create_view = TotalCartCreateView.as_view()

class TotalCartListView(ListAPIView):

    queryset = TotalCartModel.objects.all()
    serializer_class = TotalCartSerializer

    search_fields = ["title"]

total_cart_list_view = TotalCartListView.as_view()



class TotalCartUpdateView(UpdateAPIView):

    queryset = TotalCartModel.objects.all()
    serializer_class = TotalCartSerializer
    lookup_field = 'slug'

total_cart_update_view = TotalCartUpdateView.as_view()

class TotalCartDeleteView(DestroyAPIView):

    queryset = TotalCartModel.objects.all()
    serializer_class = TotalCartSerializer
    lookup_field = 'slug'

total_cart_delete_view = TotalCartDeleteView.as_view()