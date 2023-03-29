from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
Global project routes.
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

"""
Include route for static files.
"""
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
