from django.db import models
from django.urls import reverse


class News(models.Model):  # создание полей в БД
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')  # blank=true -поле не обязательное к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    # auto_now_add=True - добавляет дату создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')  # auto_now=True дата редактирования
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    # upload_to='photos/%Y/%m/%d/ - разделение фото по дате,
    # blank дает возможность делать поле не обязательным для заполнения
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):  # формирование ссылок
       return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):  # Возвращает строковое представление объекта
        return self.title

    class Meta:
        verbose_name = 'Новость'  # изменение заголовков в админке с "News" на "новость"
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']  # порядок сортировки


class Category(models.Model):  # Добавление категорий для статей
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):  # формирование ссылок
       return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):  # Возвращает строковое представление объекта
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # порядок сортировки
