from django.contrib import admin

from . import models

"""
Register models from blog application, to
django admin page.
"""
for model in [
    models.Category,
    models.Article,
]:
    admin.site.register(model)
