# Generated by Django 2.1.5 on 2019-03-08 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200)),
                ('content', models.TextField(default=None)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('publisher', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.RemoveField(
            model_name='news',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
        migrations.RemoveField(
            model_name='media',
            name='news',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.Article'),
        ),
        migrations.AddField(
            model_name='media',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='news.Article'),
        ),
    ]
