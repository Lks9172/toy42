from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accountapp.forms import CreateUserForm
from articleapp.models import Article


def index(request):
    article_list = Article.objects.all().order_by('-id')[:6]
    return render(request, 'accountapp/42toy.html', {'article_list':article_list})


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accountapp:index')