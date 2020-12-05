from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .views import (
    ProfileView,
    FavouritePosts,
    RegisterView,
)

from .forms import CustomUserCreationForm


urlpatterns = [

    path('profile/favourites/posts', FavouritePosts.as_view(), name="favourite_posts"),
    path('profile/', ProfileView.as_view(), name="profile"),

    path('login/', LoginView.as_view(template_name="home/login.html", redirect_authenticated_user=True), name="login"),

    path('register/', RegisterView.as_view(), name="register"),

    path('', include('django.contrib.auth.urls'))
    
]