from django.contrib import admin
from .models import Manga, Page, Capitel, Genres, Tom, Study

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tom)
class TomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PageInline(admin.TabularInline):
    model = Page
    extra = 10  # Количество форм для добавления страниц по умолчанию

@admin.register(Capitel)
class CapitelAdmin(admin.ModelAdmin):
    inlines = [PageInline]
    list_display = ('name', 'captel_number')
    prepopulated_fields = {'slug': ('name',)}