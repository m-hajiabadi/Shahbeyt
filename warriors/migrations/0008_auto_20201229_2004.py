# Generated by Django 3.1.3 on 2020-12-29 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warriors', '0007_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='create_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commenter',
            new_name='user',
        ),
    ]
