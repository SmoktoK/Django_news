from django.db import models


class News(models.Model):  # создание полей в БД
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)  # blank=true -поле не обязательное к заполнению
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add=True - добавляет дату создания
    updated_at = models.DateTimeField(auto_now=True)  # auto_now=True дата редактирования
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # upload_to='photos/%Y/%m/%d/ - разделение фото по дате
    is_published = models.BooleanField(default=True)

    def __str__(self):  # Возвращаяет строковое представление объекта
        return self.title
