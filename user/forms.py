from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ("username", "email")


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"readonly": True}),
            "first_name": forms.TextInput(attrs={"required": True}),
            "last_name": forms.TextInput(attrs={"required": True}),
            "email": forms.EmailInput(attrs={"required":True})
        }
        
    def clean(self):
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data["email"]
        if first_name == "" or last_name == "" or email  == "":
            raise ValidationError("Required")

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        exclude = ['user', 'favourite_posts']