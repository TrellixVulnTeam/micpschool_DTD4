# Generated by Django 2.1.5 on 2019-02-11 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]
