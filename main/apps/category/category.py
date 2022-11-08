from django.urls import path

from . import views

urlpatterns = [
    path('category-create/',view=views.category_create_view,name='category_create_view'),
    path('category-list/',view=views.category_list_view,name='category_list_view'),
]