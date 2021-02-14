from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from articleapp.views import index, ArticleDetailView, ArticleCreateView, ArticleUpdateView, MyArticleList

app_name = "articleapp"

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('index/', index, name='index'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('mylist/', MyArticleList, name='mylist'),

]