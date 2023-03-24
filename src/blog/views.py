from django.http import HttpResponseBadRequest
from django.shortcuts import render


def index(request):
    match request.method:
        case 'GET':
            template = 'blog/index.html'
            context = {}

            return render(request, template, context)

        case other:
            return HttpResponseBadRequest
