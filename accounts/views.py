from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .forms import CustomUserCreationForm, UserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'accounts/account_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        requested_profile = get_object_or_404(CustomUser, id=self.kwargs['pk'])

        context['requested_profile'] = requested_profile
        return context


class UserProfileChangeView(UpdateView):
    model = CustomUser
    success_url = reverse_lazy('home')
    template_name = 'accounts/edit_account.html'

    form_class = UserChangeForm