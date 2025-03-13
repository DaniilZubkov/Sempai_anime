from django.contrib import admin
from .models import AnimeTitle, Genres, Study, Voice, Anime

@admin.register(AnimeTitle)
class AnimeTitleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Voice)
class VoiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}