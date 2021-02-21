from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from applyapp.decorators import article_ownership_required
from applyapp.forms import ApplyForm
from applyapp.models import Apply
from articleapp.models import Article

has_ownership = [article_ownership_required, login_required]


@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class ApplyCreateView(CreateView):
    model = Apply
    form_class = ApplyForm
    template_name = 'applyapp/create.html'

    def form_valid(self, form):
        temp_apply = form.save(commit=False)
        temp_apply.applicant_id = self.request.user.id
        temp_apply.save()
        return super().form_valid(form)

    def get_success_url(self):
        print(self.request)
        return reverse('articleapp:index')


class ApplyDetailView(DetailView):
    model = Apply
    context_object_name = 'target_apply'
    template_name = 'applyapp/detail.html'



def MyApplyList(request):
    user = request.user
    applys = Apply.objects.filter(applicant_id=user.id)
    return render(request, 'applyapp/list.html', {'applys':applys})


def DecisionApply(request):
    if request.method == 'POST':
        applys = Apply.objects.filter(id=request.POST.get('id'))
        return render(request, 'applyapp/applydecision.html', {'applys': applys})


def Comment(request):
    if request.method == 'POST':
        apply = Apply.objects.filter(id=request.POST.get('id'))
        for i in apply:
            i.comment = request.POST.get('comment')
            if request.POST.get('yes'):
                i.decision = 2
            else:
                i.decision = 3
            article_id = i.offer_id
            i.save()
        article = Article.objects.filter(id=article_id)
        applys = Apply.objects.filter(offer_id=article_id)
        return render(request, 'articleapp/applylist.html', {'applys':applys, 'article':article})

