from django.db import models



class Genres(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Жанр аниме')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name




class Study(models.Model):
    name = models.CharField(max_length=100, verbose_name='Студия создатель')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name




class Manga(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image_poster = models.ImageField(upload_to='manga_images_posters/', verbose_name='Изображение')
    genre = models.ForeignKey(to=Genres, on_delete=models.CASCADE, verbose_name='Жанр')
    release_date = models.DateField(verbose_name='Дата выпуска', blank=True, null=True)
    age_limit = models.CharField(max_length=100, blank=True, verbose_name='Возрастное ограничение', null=True)
    study = models.ForeignKey(to=Study, on_delete=models.CASCADE, verbose_name='Студия создатель')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    # tom = models.ForeignKey(to=Tom, on_delete=models.CASCADE, verbose_name='Том', related_name='toms')
    # captel = models.ForeignKey(to=Capitel, on_delete=models.CASCADE, verbose_name='Глава', related_name='capitels')

    def __str__(self):
        return self.name




class Tom(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    tom_number = models.IntegerField()
    manga = models.ForeignKey(  # Изменили направление связи
        Manga,
        on_delete=models.CASCADE,
        related_name='toms',
        verbose_name='Манга'
    )

    def __str__(self):
        return self.name


class Capitel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    captel_number = models.IntegerField(verbose_name='Номер главы')

    tom = models.ForeignKey(  # Связь с томом
        Tom,
        on_delete=models.CASCADE,
        related_name='capitels',
        verbose_name='Том'
    )

    def __str__(self):
        return self.name


class Page(models.Model):
    capitel = models.ForeignKey(
        Capitel,
        on_delete=models.CASCADE,
        related_name='pages',
        verbose_name='Глава'
    )
    image = models.ImageField(
        upload_to='manga_pages/',
        verbose_name='Страница'
    )
    page_number = models.PositiveIntegerField(
        verbose_name='Номер страницы'
    )

    class Meta:
        ordering = ['page_number']

    def __str__(self):
        return f"Страница {self.page_number} - {self.capitel.name}"