from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView

from articleapp.forms import CreateArticleForm
from articleapp.models import Article, TeamMember


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

                a = Article(Publisher= request.user, title=title, Introduce=Introduce, local=Local, lapse=lapse,
                        deadline=deadline, now_pd=now_pd, now_dev=now_dev, now_designer=now_designer)
                a.save()
                TeamMember(project_id=a.id, pd=pd, dev=dev, designer=designer).save()
                return redirect('articleapp:index')
    else:
        form = CreateArticleForm()
    return render(request, 'articleapp/create.html', {'form': form})


def index(request):
    articles = Article.objects.all()
    members = TeamMember.objects.all()
    return render(request, 'articleapp/index.html', {'articles': articles, 'members': members})