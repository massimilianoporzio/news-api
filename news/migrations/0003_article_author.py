# Generated by Django 3.2.3 on 2021-05-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Mario Rossi', max_length=120),
        ),
    ]