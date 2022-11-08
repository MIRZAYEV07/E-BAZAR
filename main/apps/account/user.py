from django.urls import include, path

app_name = "account"

urlpatterns = [
    path(
        "",
        include(
            ("main.apps.account.urls.user", "main.apps.account.urls.user"),
            namespace="",
        ),
    ),


]