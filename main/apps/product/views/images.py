from django.db.models import Count
from rest_framework.generics import (ListCreateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)

from ..models.images import ProductImage
from ..serializers.images import ProductImageCreateSerializer


class ProductImageCreateView(ListCreateAPIView):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageCreateSerializer


product_image_create_view = ProductImageCreateView.as_view()

class ProductImageListView(ListAPIView):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageCreateSerializer


product_image_list_view = ProductImageListView.as_view()


class ProducImageDetailView(RetrieveAPIView):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageCreateSerializer
    lookup_field = 'slug'

product_image_detail_view = ProducImageDetailView.as_view()

class ProductImageUpdateView(UpdateAPIView):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageCreateSerializer
    lookup_field = 'slug'

product_image_update_view = ProductImageUpdateView.as_view()

class ProductImageDeleteView(DestroyAPIView):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageCreateSerializer
    lookup_field = 'slug'

product_image_delete_view = ProductImageDeleteView.as_view()