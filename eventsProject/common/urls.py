from django.urls import path
import eventsProject.common.views as views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]