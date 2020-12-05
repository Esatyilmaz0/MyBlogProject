""" Modules... """
from django.urls import path

from .views import (
    HomeView,

    AuthorPostsView,
    SearchPostsView,
    SearchPostsWithTagView,
    CategoryPostsView,
)


urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('search/', SearchPostsView.as_view(), name="search"),

    path('tag/<str:tag>', SearchPostsWithTagView.as_view(), name="tag_posts"),

    path('author/<str:username>', AuthorPostsView.as_view(), name="author"),

    path('category/<str:category_name>', CategoryPostsView.as_view(), name="category"),

]