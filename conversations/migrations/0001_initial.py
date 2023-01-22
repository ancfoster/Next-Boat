# Generated by Django 3.2.16 on 2023-01-21 18:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0011_auto_20230121_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_thumbnail', models.ImageField(upload_to='', verbose_name='Convßersation Image')),
                ('conversation_title', models.CharField(max_length=200, verbose_name='Conversation Title')),
                ('conversation_boat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='conversation_boat', to='listings.listings')),
                ('conversation_buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='conversation_buyer', to=settings.AUTH_USER_MODEL)),
                ('conversation_seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='conversation_seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conversation',
            },
        ),
        migrations.CreateModel(
            name='ConversationMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_sent', models.DateTimeField(auto_now=True)),
                ('message_contents', models.CharField(max_length=2000, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2000)], verbose_name='Message')),
                ('message_conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_conversation', to='conversations.conversations')),
                ('message_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='message_from', to=settings.AUTH_USER_MODEL)),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='message_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conversation Messages',
            },
        ),
    ]