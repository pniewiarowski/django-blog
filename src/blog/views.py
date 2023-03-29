from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseNotFound

from . import models
from . import utils


@require_http_methods(['GET'])
def index(request):
    """
    Default view for blog application.
    :param request: Given request.
    :return: Response as a rendered template.
    """
    template = 'blog/index.html'
    context = {
        'categories': models.Category.objects.filter(is_enabled=True),
        'articles': models.Article.objects.filter(is_enabled=True).order_by('-created'),
    }

    return render(request, template, context)


@require_http_methods(['GET'])
def article_details(request, primary_key):
    """
    View for display data from single Blog article.
    :param primary_key: Primary key to load Blog article, provided from URL.
    :param request: Given request.
    :return: Response as a rendered template.
    """
    article = get_object_or_404(models.Article, pk=primary_key)

    if not article.is_enabled:
        return HttpResponseNotFound(request)

    template = 'blog/article_details.html'
    context = {
        'article': utils.increment_article_views(article)
    }

    return render(request, template, context)
