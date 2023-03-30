from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [('blog', '0002_article_views')]
    operations = [
        migrations.AddField(
            model_name='article',
            name='next',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='%(class)s_next',
                to='blog.article'
            ),
        ),
        migrations.AddField(
            model_name='article',
            name='previous',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='%(class)s_previous',
                to='blog.article'
            ),
        ),
    ]
