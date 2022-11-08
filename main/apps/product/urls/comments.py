from django.urls import path

from ..views import comments

urlpatterns = [

    path('comment-create/',view=comments.comment_create_view,name='comment_create_view'),
    path('comment-list/',view=comments.comment_list_view,name='comment_list_view'),




]