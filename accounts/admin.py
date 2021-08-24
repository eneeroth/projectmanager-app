from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'is_staff'] # wich fields listed
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('age', 'bio_text', 'facebook_url', 'twitter_url', 'instagram_url', 'website_url', 'profile_pic',)}),) # edit
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('age',)}),) # add


admin.site.register(CustomUser, CustomUserAdmin)