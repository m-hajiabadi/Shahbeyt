# Generated by Django 3.1.3 on 2020-12-29 23:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warriors', '0008_auto_20201229_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislike_number',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like_number',
        ),
        migrations.AddField(
            model_name='comment',
            name='disliked_user',
            field=models.ManyToManyField(related_name='disliked_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='liked_user',
            field=models.ManyToManyField(related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]