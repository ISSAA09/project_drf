from datetime import timedelta, datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from users.models import User


@shared_task
def send_mail_notification(user_email, course_name):
    send_mail(
        subject=f'Обновление курса {course_name}',
        message=f'Дорогой пользователь, материалы курса {course_name} были обновлены. Проверьте новый контент на нашем сайте.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email]
    )


@shared_task
def block_user():
    required_date = datetime.now() - timedelta(days=30.5)
    inactive_users = User.objects.filter(last_login__lt=required_date, is_active=True)
    for user in inactive_users:
        user.is_active = False
        user.save()
