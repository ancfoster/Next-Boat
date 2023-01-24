# Generated by Django 3.2.16 on 2023-01-24 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0012_alter_listings_total_hp'),
        ('conversations', '0004_remove_conversations_conversation_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessages',
            name='message_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conversationmessages',
            name='message_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conversations',
            name='conversation_boat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_boat', to='listings.listings'),
        ),
        migrations.AlterField(
            model_name='conversations',
            name='conversation_buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conversations',
            name='conversation_seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
