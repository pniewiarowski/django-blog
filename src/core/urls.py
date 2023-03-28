from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
Global project routes.
"""
urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]

# Include routes for static files.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
