# Generated by Django 3.2.16 on 2023-01-23 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20230123_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversations',
            name='last_message_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last message date'),
        ),
    ]
