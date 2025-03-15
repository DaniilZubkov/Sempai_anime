from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Genres(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Жанр аниме')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name

class Voice(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Озвучка')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name

class Study(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Студия Создатель')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название аниме')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    genre = models.ForeignKey(to=Genres, on_delete=models.CASCADE, verbose_name='Жанр')
    release_date = models.DateField(verbose_name='Дата выпуска', blank=True, null=True)
    study = models.ForeignKey(to=Study, on_delete=models.CASCADE, verbose_name='Студия')
    image = models.ImageField(upload_to='anime_images/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    mpaa = models.CharField(max_length=100, blank=True, null=True, verbose_name='MPAA')
    age_limit = models.CharField(max_length=100, blank=True, verbose_name='Возрастное ограничение', null=True)
    lang = models.CharField(max_length=100, blank=True, verbose_name='Длительность серии', null=True)


    def __str__(self):
        return self.name



class AnimeTitle(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Тайтл')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    genre = models.ForeignKey(to=Genres, on_delete=models.CASCADE, verbose_name='Жанр')
    release_date = models.DateField(verbose_name='Дата выпуска', blank=True, null=True)
    image = models.ImageField(upload_to='anime_images/', verbose_name='Изображение')
    mpaa = models.CharField(max_length=100, blank=True, null=True, verbose_name='MPAA')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    voice = models.ForeignKey(to=Voice, on_delete=models.CASCADE, verbose_name='Озвучка')
    study = models.ForeignKey(to=Study, on_delete=models.CASCADE, verbose_name='Студия')
    age_limit = models.CharField(max_length=100, blank=True, verbose_name='Возрастное ограничение', null=True)
    status = models.CharField(max_length=100, blank=True, verbose_name='Статус', null=True)
    lang = models.CharField(max_length=100, blank=True, verbose_name='Длительность серии', null=True)
    year = models.DateField()
    anime = models.ForeignKey(to=Anime, on_delete=models.CASCADE, verbose_name='Аниме (отношение)', related_name='episodes')
    episode_numer = models.IntegerField()
    vidio_file = models.FileField(
        upload_to='videos/',
        validators=[
            FileExtensionValidator(['mp4', 'avi', 'wmv', 'flv', 'webm'])
        ]
    )
    uploaded_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.anime.name} - Episode {self.episode_numer}: {self.name}"



