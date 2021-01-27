from django.urls import path, include

from accountapp.views import AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
    ]