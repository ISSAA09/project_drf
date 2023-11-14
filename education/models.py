from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='превью')
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name='user',
                             related_name='course')

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
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user', blank=True, null=True,
                             related_name='lessons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
