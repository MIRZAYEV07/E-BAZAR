from django.db.models import Count
from rest_framework.generics import (ListCreateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)

from ..models.product import ProductModel
from ..serializers.product import ProductCreateSerializers,ProductListSerializers


class ProductCreateView(ListCreateAPIView):

    queryset = ProductModel.objects.all()
    serializer_class = ProductCreateSerializers


product_create_view = ProductCreateView.as_view()

class ProductListView(ListAPIView):

    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializers
    filterset_fields = ["title", "category"]
    search_fields = ["title"]

product_list_view = ProductListView.as_view()


class ProducDetailView(RetrieveAPIView):

    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializers
    lookup_field = 'slug'

product_detail_view = ProducDetailView.as_view()

class ProductUpdateView(UpdateAPIView):

    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializers
    lookup_field = 'slug'

product_update_view = ProductUpdateView.as_view()

class ProductDeleteView(DestroyAPIView):

    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializers
    lookup_field = 'slug'

product_delete_view = ProductDeleteView.as_view()

class NewAddedProductListView(ListAPIView):

    queryset = ProductModel.objects.all().order_by('-created_at')
    serializer_class = ProductListSerializers


new_added_product_list = NewAddedProductListView.as_view()

class MostViewedProductListView(ListAPIView):

    queryset = ProductModel.objects.annotate(sum_of_comments=Count('comments')).order_by('-sum_of_comments')
    serializer_class = ProductListSerializers

most_viewed_product_list = MostViewedProductListView.as_view()

class ProductInSaleListView(ListAPIView):

    queryset = ProductModel.objects.retrieve_products_in_sale()
    serializer_class = ProductListSerializers

product_in_sale_list = ProductInSaleListView.as_view()