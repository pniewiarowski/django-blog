from django.http import HttpResponseBadRequest
from django.shortcuts import render

from . import models


def index(request):
    """
    Default view for blog application.
    :param request: Given request.
    :return: Response as a rendered template.
    """
    match request.method:
        case 'GET':
            template = 'blog/index.html'
            context = {
                'categories': models.Category.objects.filter(is_enabled=True),
                'articles': models.Article.objects.filter(is_enabled=True),
            }

            return render(request, template, context)

        case other:
            return HttpResponseBadRequest
