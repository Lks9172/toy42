from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from applyapp.forms import ApplyForm
from applyapp.models import Apply
from articleapp.models import Article


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
        return reverse('articleapp:index')

class ApplyDetailView(DetailView):
    model = Apply
    context_object_name = 'target_apply'
    template_name = 'applyapp/detail.html'


def MyApplyList(request):
    user = request.user
    applys = Apply.objects.filter(applicant_id=user.id)
    return render(request, 'applyapp/list.html', {'applys':applys})

