from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accountapp.forms import CreateUserForm
from articleapp.models import Article, TeamMember


def index(request):
    article_list = Article.objects.all()[:6]
    members = TeamMember.objects.all()
    return render(request, 'accountapp/42toy.html', {
                                                     'members': members,  'article_list':article_list})


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accountapp:index')