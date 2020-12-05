from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.cache import cache
from django.views.generic import ListView

from post.models import Post

from .sub_models.Category import Category



class HomeMixin:
    context_object_name = "posts"
    template_name       = "home/blog_grid.html"
    paginate_by         = 10


class HomeView(HomeMixin, ListView):
    """
        Tüm Postları Anasayfada Görüntüler
    """
    
    queryset = Post.objects.select_related("author", "category").all()
    

class AuthorPostsView(HomeMixin, ListView):

    """
        Url'den Kullanıcı Adı Gelen Yazarın Postlarını Getirir.
    """

    def get_queryset(self, *args, **kwargs):
        author_posts = User\
            .objects\
            .prefetch_related("posts")\
            .get(username=self.kwargs["username"])\
            .posts\
            .all()

        return author_posts


class SearchPostsView(HomeMixin, ListView):

    """
        Search Posts By Query String
        GET: /search
        Query String: q
    """
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        posts = Post\
            .objects\
            .select_related("author", "category")\
            .filter(title__contains=query)
        return posts


class CategoryPostsView(HomeMixin, ListView):

    """
        Search Posts By Category
        GET : /category/params
        Params:
            @category_name: A Category Name
    """

    def get_queryset(self, *args, **kwargs):
        category_posts = Category\
            .objects\
            .prefetch_related("posts")\
            .get(slug__iexact=self.kwargs["category_name"])\
            .posts\
            .all()

        return category_posts


class SearchPostsWithTagView(HomeMixin, ListView):

    """
        Search Posts By Tag
        GET : /search
        Params: tag
    """

    def get_queryset(self, *args, **kwargs):
        tag = self.kwargs["tag"]
        posts = Post\
            .objects\
            .select_related("author", "category")\
            .all()

        filtered_posts = [filtered_post for filtered_post in posts if tag in filtered_post.tags.split(",")]
        return filtered_posts
