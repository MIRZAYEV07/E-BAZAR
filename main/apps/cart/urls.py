from django.urls import path
from . import views

urlpatterns = [
    path(
        'cart-create/',
        view = views.cart_create_view,
        name = 'cart_create'
    ),

    path(
        'cart-list/',
        view = views.cart_list_view,
        name = 'cart_list'
    ),

    path(
        'cart-update/',
        view = views.cart_update_view,
        name = 'cart_update'
    ),

    path(
        'cart-delete/',
        view = views.cart_delete_view,
        name='cart_update'
    ),


    path(
        'total-cart-create/',
        view=views.total_cart_create_view,
        name='total_cart_create'
    ),

    path(
        'total-cart-list/',
        view=views.total_cart_list_view,
        name='total_cart_list'
    ),

    path(
        'total-cart-update/',
        view=views.total_cart_update_view,
        name='total_cart_update'
    ),

    path(
        'total-cart-delete/',
        view=views.total_cart_delete_view,
        name='total_cart_update'
    )
]