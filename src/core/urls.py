from django.contrib import admin
from django.urls import path, include

"""
Global project routes.
"""
urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]
