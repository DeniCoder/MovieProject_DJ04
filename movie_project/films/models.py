from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    review = models.TextField(verbose_name='Отзыв о фильме')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв о фильме'
        verbose_name_plural = 'Отзывы о фильмах'