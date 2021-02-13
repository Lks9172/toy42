from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView, DetailView

from articleapp.forms import CreateArticleForm
from articleapp.models import Article


def createproject(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                title = form.cleaned_data['title']
                Introduce = form.cleaned_data['Introduce']
                Local = form.cleaned_data['Local']
                lapse = form.cleaned_data['lapse']
                deadline = form.cleaned_data['deadline']
                now_pd = form.cleaned_data['now_pd']
                now_dev = form.cleaned_data['now_dev']
                now_designer = form.cleaned_data['now_designer']

                # for TeamMember
                pd = form.cleaned_data['pd']
                dev = form.cleaned_data['dev']
                designer = form.cleaned_data['designer']

                a = Article(publisher= request.user, title=title, Introduce=Introduce, local=Local, lapse=lapse,
                        deadline=deadline, now_pd=now_pd, now_dev=now_dev, now_designer=now_designer)
                a.save()
                return redirect('articleapp:index')
    else:
        form = CreateArticleForm()
    return render(request, 'articleapp/create.html', {'form': form})


def index(request):
    article_list = Article.objects.all()
    return render(request, 'articleapp/index.html', {'article_list':article_list})


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'