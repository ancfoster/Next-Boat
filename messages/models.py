from django.db import models
from .models import Listings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

# Create your models here.
class Conversations(models.Model):
    conversation_boat = models.ForeignKey(Listings)
    conversation_buyer = models.ForeignKey(User)
    conversation_seller = models.ForeignKey(User)
    conversation_thumbnail = models.ImageField(verbose_name='Conversation Image')
    conversation_title = models.CharField(max_length=120, verbose_name="Conversation Title")
    last_message_date = models.DateTimeField

class Messages(models.Model):
    message_conversation = models.ForeignKey(Conversations)
    message_sent = models.DateTimeField(auto_now=True)
    message_from = models.ForeignKey(User)
    message_to = models.ForeignKey(User)
    message_contents = models.CharField(validators=[MinValueValidator(1), MaxValueValidator(2000)], verbose_name='Message')

