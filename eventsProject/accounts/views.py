from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from eventsProject.accounts.forms import BaseUserCreationForm

UserModel = get_user_model()


class LoginUserView(LoginView):
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
