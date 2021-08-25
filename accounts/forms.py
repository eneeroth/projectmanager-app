from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Changes the built-in UserCreationForm and adds some additional fields¨
    Meta class overrides defaults
    """
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age',) # UserCreationForm contains username and password


class UserChangeForm(ModelForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'profile_pic', 'bio_text', 'first_name', 'last_name', 'email', 'age',
            'facebook_url', 'twitter_url', 'instagram_url', 'website_url',)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3',}),
            # 'profile_pic': forms.FileInput(attrs={'class': 'form-control mb-3',}),
            'bio_text': forms.Textarea(attrs={'class': 'form-control mb-3',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-3',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-3',}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3',}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control mb-3',}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control mb-3',}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control mb-3',}),
            'website_url': forms.URLInput(attrs={'class': 'form-control mb-3',}),
        }

        labels = {
            'profile_pic': 'Profile picture',
        }