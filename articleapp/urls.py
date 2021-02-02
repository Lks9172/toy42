from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from accountapp.views import index, CreateUserView
from articleapp.views import createproject

app_name = "articleapp"

urlpatterns = [
    path('create/', createproject, name='create'),
]