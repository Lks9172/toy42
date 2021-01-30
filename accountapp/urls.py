from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from accountapp.views import index, CreateUserView

app_name = "accountapp"

urlpatterns = [
    path('', index, name='index'),
    path('Logout/', LogoutView.as_view(), name='logout'),
    path('Login/', LoginView.as_view(), name='login'),
    path('create/', CreateUserView.as_view(), name='signup'),
]