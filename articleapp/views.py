from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models.fields.related import RelatedField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView

from applyapp.models import Apply
from articleapp.decorators import article_ownership_required
from articleapp.forms import CreateArticleForm
from articleapp.models import Article


def index(request):
    article_list = Article.objects.all().order_by('-id')
    return render(request, 'articleapp/index.html', {'article_list':article_list})


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = CreateArticleForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.publisher_id = self.request.user.id
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = CreateArticleForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})


def MyArticleList(request):
    user = request.user
    articles = Article.objects.filter(publisher_id=user.id)
    return render(request, 'articleapp/list.html', {'articles':articles})

def ArticleApplyList(request):
    a = request.POST.get('id')
    article = Article.objects.filter(id=a)
    applys = Apply.objects.filter(offer_id=a)
    return render(request, 'articleapp/applylist.html', {'applys':applys, 'article':article})

