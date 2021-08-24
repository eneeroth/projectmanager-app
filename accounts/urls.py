from django.urls import path

from .views import SignUpView, UserProfileView, UserProfileChangeView


urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile_page'),
    path('profile/<int:pk>/edit', UserProfileChangeView.as_view(), name='profile_edit')
]