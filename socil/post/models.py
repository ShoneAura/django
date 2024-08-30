from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts', verbose_name="Автор")
    content = models.TextField(verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
