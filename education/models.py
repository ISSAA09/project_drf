from django.db import models
from django.utils.timezone import now

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='превью')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='превью')
    video_link = models.URLField(blank=True, null=True, verbose_name='видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, verbose_name='курс')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    PAYMENT_TYPE = (
        ('cash', 'наличные'),
        ('transfer', 'перевод')
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь', blank=True, null=True)
    date_payment = models.DateField(default=now)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', blank=True, null=True)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_type = models.CharField(choices=PAYMENT_TYPE, verbose_name='тип оплаты', max_length=10)

    def __str__(self):
        return f'{self.user} {self.payment_type} {self.date_payment}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
