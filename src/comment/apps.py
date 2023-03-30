from django.apps import AppConfig


class CommentConfig(AppConfig):
    """
    Comment application configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comment'
