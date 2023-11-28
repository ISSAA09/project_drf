# Generated by Django 4.2.7 on 2023-11-28 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='stripe_payment_id',
            field=models.CharField(max_length=150, null=True, unique=True, verbose_name='платеж'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_payment',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
