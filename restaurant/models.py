from django.db import models

class Blog(models.Model):
    name = models.CharField(
        max_length=255555,
        db_index=True,
        blank=True,
        verbose_name='name'
    )
    age = models.IntegerField(
        blank=True,
        default=0,
        verbose_name='age'
    )
    salary = models.IntegerField(
        blank=True,
        default=0,
        verbose_name='salary'
    )
    skill = models.CharField(
        max_length=255555,
        db_index=True,
        blank=True,
        verbose_name='skill'
    )
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        blank=True,
        verbose_name='Фотки'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    public = models.BooleanField(
        default=True,
        verbose_name='Опубликованно'
    )
