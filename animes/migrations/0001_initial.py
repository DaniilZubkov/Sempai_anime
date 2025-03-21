# Generated by Django 5.0.6 on 2025-03-09 08:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Жанр аниме')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Студия Создатель')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Озвучка')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название аниме')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выпуска')),
                ('image', models.ImageField(upload_to='anime_images/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('mpaa', models.CharField(blank=True, max_length=100, null=True, verbose_name='MPAA')),
                ('age_limit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Возрастное ограничение')),
                ('lang', models.CharField(blank=True, max_length=100, null=True, verbose_name='Длительность серии')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.genres', verbose_name='Жанр')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.study', verbose_name='Студия')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Тайтл')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выпуска')),
                ('image', models.ImageField(upload_to='anime_images/', verbose_name='Изображение')),
                ('mpaa', models.CharField(blank=True, max_length=100, null=True, verbose_name='MPAA')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('age_limit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Возрастное ограничение')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Статус')),
                ('lang', models.CharField(blank=True, max_length=100, null=True, verbose_name='Длительность серии')),
                ('year', models.DateField()),
                ('episode_numer', models.IntegerField()),
                ('vidio_file', models.FileField(upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi', 'wmv', 'flv', 'webm'])])),
                ('uploaded_at', models.DateField(auto_now_add=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.anime', verbose_name='Аниме (отношение)')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.genres', verbose_name='Жанр')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.study', verbose_name='Студия')),
                ('voice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.voice', verbose_name='Озвучка')),
            ],
        ),
    ]
