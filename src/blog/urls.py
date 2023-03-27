from django.urls import path

from . import views

"""
Register routes for blog application.
"""
urlpatterns = [
    path('', views.index, name='blog-index'),
]
