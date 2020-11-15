# Generated by Django 3.1.3 on 2020-11-15 22:07

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=50)),
                ('admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
