from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseNotFound

from . import models


@require_http_methods(['GET'])
def index(request):
    """
    View to render all comments from system.
    :param request: Given request.
    :return: Response as a rendered template.
    """
    template = 'comment/all.html'
    context = {}

    return render(request, template, context)


@require_http_methods(['GET'])
def comment_details(request, primary_key):
    """
    View for display data from single Comment.
    :param primary_key: Primary key to load Blog article, provided from URL.
    :param request: Given request.
    :return: Response as a rendered template.
    """
    comment = get_object_or_404(models.Comment, pk=primary_key)

    if not comment.is_enabled:
        return HttpResponseNotFound(request)

    template = 'comment/comment_details.html'
    context = {
        'comment': comment,
    }

    return render(request, template, context)
