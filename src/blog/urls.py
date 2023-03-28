from django.urls import path

from . import views

"""
Register routes for blog application.
"""
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('article/<int:primary_key>/', views.article_details, name='blog-article-details'),
]
