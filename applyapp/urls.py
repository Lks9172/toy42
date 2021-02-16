from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from applyapp.views import ApplyCreateView, MyApplyList, ApplyDetailView, DecisionApply, Comment
from articleapp.views import index, ArticleDetailView, ArticleCreateView, ArticleUpdateView, MyArticleList

app_name = "applyapp"

urlpatterns = [
    path('create/', ApplyCreateView.as_view(), name='create'),
    path('list/', MyApplyList, name='list'),
    path('detail/<int:pk>', ApplyDetailView.as_view(), name='detail'),
    path('decision/', DecisionApply, name='decision'),
    path('comment/', Comment, name='comment'),

]