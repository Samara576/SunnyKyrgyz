from django.db import models
from django.utils.text import slugify

from apps.travel.service import compress_image


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='news', verbose_name='Изображение новости', blank=True, null=True)
    content = models.TextField(verbose_name="Содержание")
    published_date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на источник")
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="человеко-понятный url",
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

        if self.image:
            self.compress_image()

    def compress_image(self):
        return compress_image(self)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
