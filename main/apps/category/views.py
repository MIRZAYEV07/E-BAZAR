from rest_framework.generics import ListAPIView,CreateAPIView

from .serializers import CategoryCreateSerializer
from .models import Category

class CategoryListApiView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

category_list_view = CategoryListApiView.as_view()

class CategoryCreateAPIview(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

category_create_view = CategoryCreateAPIview.as_view()


