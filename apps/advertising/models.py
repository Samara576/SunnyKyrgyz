from django.db import models
from django.utils.text import slugify

from apps.travel.models import Housing


class Advertising(models.Model):
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, verbose_name="Место жительства")
    added = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="человеко-понятный url", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.housing)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.housing

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"
