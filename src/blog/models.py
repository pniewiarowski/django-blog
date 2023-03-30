from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Category(models.Model):
    """
    Model data class for blog category
    """
    is_enabled = models.BooleanField(default=True)
    title = models.CharField(max_length=64, unique=True, blank=False, null=False)
    short_description = models.TextField(max_length=1024, default="", blank=True, null=True)

    class Meta:
        """
        Category model meta class.
        """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
        Return string representation of a Category model.
        :return: Category instance string representation.
        """
        return f'{self.title}'


class Article(models.Model):
    """
    Model data class for blog article.
    """
    is_enabled = models.BooleanField(default=True, blank=False, null=False)
    title = models.CharField(max_length=64, unique=True, blank=False, null=False)
    short_description = models.TextField(max_length=255, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=f'uploads/blog/thumbnail/', blank=True, null=True)
    main_content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now, blank=False, null=False)
    views = models.IntegerField(default=0, blank=False, null=False, validators=[MinValueValidator(0)])
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, blank=True, null=True)
    next = models.ForeignKey(to='self', related_name='%(class)s_next', on_delete=models.SET_NULL, blank=True, null=True)
    previous = models.ForeignKey(to='self', related_name='%(class)s_previous', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        """
        Article model meta class.
        """
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """
        Return string representation of an Article model.
        :return: Article instance string representation.
        """
        return f'{self.title}'

    def increment_views(self):
        """
        Update views for current article instance.
        :return: Current updated instance.
        """
        self.views += 1
        self.save()

        return self
