from django.urls import path

from ..views import product

urlpatterns = [
    path(
        "product-create/",
        view=product.product_create_view,
        name="product_create"
    ),
    path(
        "product-list/",
        view=product.product_list_view,
        name="product_list"
    ),
    path(
        "product-detail/<str:slug>/",
        view=product.product_detail_view,
        name="product_detail"
    ),
    path(
        "product-update/<str:slug>/",
        view=product.product_update_view,
        name="product_update"
    ),
    path(
        "product-delete/<str:slug>/",
        view=product.product_delete_view,
        name="product_delete"
    ),
     path(
        "new-added-product/",
        view=product.new_added_product_list,
        name="new_added_product"
    ),
    path(
        "most-viewed-product/",
        view=product.most_viewed_product_list,
        name="most_viewed_product"
    ),
    path(
        "product-in-sale/",
        view=product.product_in_sale_list,
        name="product_in_sale_list"
    ),





]
