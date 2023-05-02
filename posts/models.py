import datetime

from django.db import models
from django.utils.timezone import now
# Create your models here.


class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    title = models.TextField(max_length=200, default='Lorem ipsum', verbose_name='Заголовок')
    body = models.TextField(default='Lorem ipsum', verbose_name='Tекст')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(default=now)
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return self.title

