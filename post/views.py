from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView
from user.models import UserProfile
from .models import Post, Comment
from django.shortcuts import render

class PostView(DetailView):
    template_name = 'home/blog_single.html'
    context_object_name = "post"

    def get_object(self):
        return Post.objects.get(slug=self.kwargs["slug"])

    def post(self, *args, **kwargs):
        """
        
            Add Comment
        """
        post_object = Post.objects.get(id=self.request.POST.get("post_id"))
        new_comment = Comment(author=self.request.user, content=self.request.POST.get("comment"), post=post_object)
        try:
            new_comment.save()
            return render(self.request, template_name=self.template_name, context={"post":post_object})
        except ValidationError as err:
            return render(self.request, self.template_name, {"post":post_object, "error":err.message})


def delete_comment(request):
    

    if request.method == "POST":
        comment_id = request.POST.get("comment_id")
        comment = Comment.objects.get(id=comment_id).delete()
        return JsonResponse({"Code":"200", "Message":"Deleted Comment"})
    return JsonResponse({"Code":"404"})