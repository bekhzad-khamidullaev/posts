from django.db import models

# Create your models here.


class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    last_changes = models.CharField(max_length=50, verbose_name='Последнее изменение')
    text = models.TextField(verbose_name='Пост')
    author = models.TextField(verbose_name="Автор", max_length=140)


    def __str__(self):
        return self.text
