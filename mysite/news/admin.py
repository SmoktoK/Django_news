from django.contrib import admin

# Register your models here.
from .models import News


class NewsAdmin(admin.ModelAdmin):  # настройка отображения списков в админке
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title') # добавление ссылок
    search_fields = ('title', 'content')  # включение поиска в админке

admin.site.register(News, NewsAdmin) # Регистрация приложения в админке