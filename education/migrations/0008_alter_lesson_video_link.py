# Generated by Django 4.2.7 on 2023-11-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0007_alter_lesson_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video_link',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='видео'),
        ),
    ]