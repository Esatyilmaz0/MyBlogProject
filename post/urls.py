from django.urls import path

from post.views import PostView, delete_comment

urlpatterns = [

    path('post/<str:slug>', PostView.as_view(), name="post"),
    path('delete_comment/', delete_comment, name="delete_comment")
    #path('add/comment', AddComment.as_view(), name="add_comment")
]