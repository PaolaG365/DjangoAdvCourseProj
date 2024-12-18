from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from eventsProject.accounts.forms import BaseUserCreationForm, UserProfileEditForm
from eventsProject.accounts.models import UserProfile

UserModel = get_user_model()


class BaseUserLoginUserView(LoginView):
    model = UserModel
    template_name = 'accounts/login-page.html'
    redirect_authenticated_user = True


class BaseUserRegisterView(CreateView):
    model = UserModel
    form_class = BaseUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserProfile
    template_name = 'accounts/account-delete-page.html'
    success_url = reverse_lazy('login')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        profile = get_object_or_404(UserProfile, slug=self.kwargs['slug'])
        return self.request.user == profile.user


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'accounts/account-details-page.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileEditForm
    template_name = 'accounts/account-edit-page.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        profile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy('details-profile', kwargs={'slug': self.object.slug})
