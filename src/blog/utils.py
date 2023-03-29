from . import models
from .models import Article


def increment_article_views(article: models.Article) -> Article:
    """
    Update views for given article instance.
    :param article: Article to update.
    :return: Updated article instance.
    """
    article.views += 1
    article.save()

    return article
