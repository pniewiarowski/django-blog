from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from blog import models as blog_models


class Comment(models.Model):
    """
    Model data class for comment.
    """
    is_enabled = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now, blank=False, null=False)
    content = models.TextField(max_length=1024, blank=False, null=False, validators=[MinLengthValidator(3)])
    related_article = models.ForeignKey(to=blog_models.Article, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        """
        Comment model meta class.
        """
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """
        Return string representation of a Comment model.
        :return: Comment instance string representation.
        """
        return f'Comment: {self.id}'
