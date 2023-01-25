# Generated by Django 3.2.16 on 2023-01-25 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourites',
            name='favourite_created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favourite_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favourites',
            name='favourite_created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]