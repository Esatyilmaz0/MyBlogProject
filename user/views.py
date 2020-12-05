from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import ProfileForm, CustomUserChangeForm, CustomUserCreationForm
from .models import UserProfile

class RegisterView(CreateView):
    template_name = "home/sign_up.html"
    form_class = CustomUserCreationForm
    success_url = "/accounts/profile"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
            Log In 
        """

        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

class ProfileView(LoginRequiredMixin, UpdateView):
    login_url = "/accounts/login"
    template_name = "home/profile.html"
    form_class = ProfileForm
    success_url = "/accounts/profile"

    def form_valid(self, form):
        
        user_change = CustomUserChangeForm(self.request.POST, instance=self.request.user)
        if user_change.is_valid() and form.is_valid():
            user_change.save()
            messages.success(self.request, "Your profile information has been successfully changed")
       
        else:
            messages.error(self.request, "Please do not take illegal action.")
        return super().form_valid(form)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_change_form"] = CustomUserChangeForm(instance=self.request.user)
        return context

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)


class FavouritePosts(LoginRequiredMixin, ListView):
    """
        Get My Favourite Posts
    """
    login_url = "/accounts/login"
    context_object_name = "posts"
    template_name = "home/blog_grid.html"
    paginate_by = 10
    
    def get_queryset(self):
        user = UserProfile.objects.get(user=self.request.user)

        favourite_posts = user.favourite_posts.all()
        return favourite_posts

def add_favourite_post(request):

    user = UserProfile.objects.get(user__username=request.POST.get("user"))

    post = Post.objects.get(title=request.POST.get("post_title"))

    try:
        """
            If post in user favourite posts
            remove post for user favourite posts
        """
        user_favourite_post = user.favourite_posts.get(title=post.title)
        user.favourite_posts.remove(user_favourite_post)

    except Post.DoesNotExist:
        """
            If post not in user favourite posts
            add post for user favourite posts
        """
        user.favourite_posts.add(post)


    return JsonResponse({"msg": "success"})