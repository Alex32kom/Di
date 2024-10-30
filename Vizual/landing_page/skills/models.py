from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name='Навык')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='skills_images/', verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

