from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from articleapp.views import createproject,index

app_name = "articleapp"

urlpatterns = [
    path('create/', createproject, name='create'),
    path('index/', index, name='index'),

]