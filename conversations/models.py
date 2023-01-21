from django.db import models
from listings.models import Listings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

# Create your models here.
class Conversations(models.Model):
    conversation_boat = models.ForeignKey(Listings, on_delete=models.DO_NOTHING, related_name='conversation_boat')
    conversation_buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='conversation_buyer')
    conversation_seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='conversation_seller')
    conversation_thumbnail = models.ImageField(verbose_name='Convßersation Image')
    conversation_title = models.CharField(max_length=200, verbose_name="Conversation Title")
    last_message_date = models.DateTimeField

    class Meta:
        verbose_name = "Conversation"
    def __str__(self):
        return f"{self.conversation}"

class ConversationMessages(models.Model):
    message_conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE, related_name='message_conversation')
    message_sent = models.DateTimeField(auto_now=True)
    message_from = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='message_from')
    message_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='message_to')
    message_contents = models.CharField(max_length=2000, validators=[MinValueValidator(1), MaxValueValidator(2000)], verbose_name='Message')

    class Meta:
        verbose_name = "Conversation Messages"
    def __str__(self):
            return f"{self.conversation_message}"
