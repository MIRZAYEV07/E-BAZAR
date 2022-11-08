from django.urls import path

from ..views import images

urlpatterns = [
    path(
        "image-create/",
        view=images.product_image_create_view,
        name="image_create"
    ),
    path(
        "image-list/",
        view=images.product_image_list_view,
        name="image_list"
    ),
    path(
        "product-detail/<str:slug>/",
        view=images.product_image_detail_view,
        name="image_detail"
    ),
    path(
        "image-update/<str:slug>/",
        view=images.product_image_update_view,
        name="image_update"
    ),
    path(
        "image-delete/<str:slug>/",
        view=images.product_image_delete_view,
        name="image_delete"
    ),





]
