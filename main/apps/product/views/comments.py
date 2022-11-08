from rest_framework.generics import ListAPIView,CreateAPIView

from ..models.comments import Comments
from ..models.product import ProductModel
from ..serializers.comments import CommentCreateSerializer,CommentListSerializer

class CommentCreateAPIView(CreateAPIView):

    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer

    lookup_field = "slug"

    def perform_update(self, serializer,slug):
        product = ProductModel.objects.filter(slug=slug)
        product.comments.add(serializer.validated_data)
        product.save

comment_create_view = CommentCreateAPIView.as_view()

class CommentListAPIView(ListAPIView):

    queryset = Comments.objects.all()
    serializer_class = CommentListSerializer

comment_list_view = CommentListAPIView.as_view()