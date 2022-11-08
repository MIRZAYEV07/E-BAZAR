from django.urls import include, path

app_name = "e-bazar"

urlpatterns = [
    path(
        "",
        include(
            ("main.apps.product.urls.product", "main.apps.product.urls.product"),
            namespace="",
        ),
    ),
    path(
        "main-feature/",
        include(
            ("main.apps.product.urls.main_features", "main.apps.product.urls.main_features"),
            namespace="main_features",
        ),
    ),
    path(
        "sub-feature/",
        include(
            ("main.apps.product.urls.sub_features", "main.apps.product.urls.sub_features"),
            namespace="sub_features",
        ),
    ),
    path(
        "comment/",
        include(
            ("main.apps.product.urls.comments", "main.apps.product.urls.comments"),
            namespace="comment",
        ),
    ),
    path(
        "images/",
        include(
            ("main.apps.product.urls.images", "main.apps.product.urls.images"),
            namespace="images",
        ),
    ),

]
