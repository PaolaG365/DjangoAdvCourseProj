from django.contrib.auth.views import LogoutView
from django.urls import path, include
from eventsProject.accounts import views


urlpatterns = [
    path('register/', views.BaseUserRegisterView.as_view(), name='register'),
    path('login/', views.BaseUserLoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<slug:slug>/', include([
        path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
        path('details/', views.ProfileDetailView.as_view(), name='details-profile'),
        ])
    ),
]