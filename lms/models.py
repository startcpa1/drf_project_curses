from django.db import models
from django.utils import timezone

from config import settings
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='lms/static/images', verbose_name='картинка')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lms/static/images', verbose_name='картинка')
    url = models.URLField(max_length=150, verbose_name='ссылка')
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name='курс', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Безналичная оплата'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)
    payment_date = models.DateTimeField(default=timezone.now(), verbose_name='дата оплаты')
    payment_course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, **NULLABLE)
    amount = models.FloatField(verbose_name='сумма')

    payment_method = models.CharField(max_length=20, verbose_name='способ оплаты', choices=PAYMENT_CHOICES,
                                      default='cash')

    def __str__(self):
        return f'{self.user} {self.payment_method}'

    class Meta:
        ordering = ('payment_date',)
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
