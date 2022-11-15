from django.urls import include, path


urlpatterns = [
    path(
        "account/",
        include(
            ("main.apps.account.user", "main.apps.account.user"),
            namespace="account",
        ),
    ),
    path(
        "category/",
        include(
            ("main.apps.category.category", "main.apps.category.category"),
            namespace="category",
        ),
    ),
    path(
        "product/",
        include(
            ("main.apps.product.product", "main.apps.product.product"),
            namespace="product",
        ),
    ),
    path(
            "cart/",
            include(
                ("main.apps.cart.urls", "main.apps.cart.urls"),
                namespace="cart",
            ),
        ),

]
