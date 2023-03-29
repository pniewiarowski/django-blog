from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

"""
Register routes for blog application.
"""
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('article/<int:primary_key>/', views.article_details, name='blog-article-details'),
]

"""
Include route for uploaded files. 
"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
