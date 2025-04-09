# Generated by Django 5.0.6 on 2025-03-30 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capitel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('captel_number', models.IntegerField(verbose_name='Номер главы')),
            ],
        ),
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
                ('name', models.CharField(max_length=100, verbose_name='Студия создатель')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='manga_pages/', verbose_name='Страница')),
                ('page_number', models.PositiveIntegerField(verbose_name='Номер страницы')),
                ('capitel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='manga.capitel', verbose_name='Глава')),
            ],
            options={
                'ordering': ['page_number'],
            },
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('image_poster', models.ImageField(upload_to='manga_images_posters/', verbose_name='Изображение')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выпуска')),
                ('age_limit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Возрастное ограничение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.genres', verbose_name='Жанр')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.study', verbose_name='Студия создатель')),
            ],
        ),
        migrations.CreateModel(
            name='Tom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('tom_number', models.IntegerField()),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toms', to='manga.manga', verbose_name='Манга')),
            ],
        ),
        migrations.AddField(
            model_name='capitel',
            name='tom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitels', to='manga.tom', verbose_name='Том'),
        ),
    ]
