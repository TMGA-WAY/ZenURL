# Generated by Django 5.1.1 on 2025-01-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=50, unique=True)),
                ('long_url', models.URLField(max_length=2000)),
                ('user_id', models.IntegerField()),
                ('is_public', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
