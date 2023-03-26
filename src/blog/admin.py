from django.contrib import admin

from . import models

for model in [
    models.Category,
    models.Article,
]:
    admin.site.register(model)
