from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from articleapp.views import createproject, index, ArticleDetailView

app_name = "articleapp"

urlpatterns = [
    path('create/', createproject, name='create'),
    path('index/', index, name='index'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),

]