from django.http import HttpResponseForbidden
from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.publisher == request.user:
            return HttpResponseForbidden("잘못된 접근 입니다.")
        return func(request, *args, **kwargs)
    return decorated
