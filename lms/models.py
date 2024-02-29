from django.db import models

from config import settings


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='lms/static/images', verbose_name='картинка')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lms/static/images', verbose_name='картинка')
    url = models.CharField(max_length=150, verbose_name='ссылка')
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='курс', null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


