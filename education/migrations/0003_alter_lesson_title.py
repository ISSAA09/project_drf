# Generated by Django 4.2.7 on 2023-11-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=150, verbose_name='название'),
        ),
    ]