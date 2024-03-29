from django.db import models
from listings.models import Listings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator  # noqa
from django.utils import timezone


# Create your models here.
class Conversations(models.Model):
    conversation_boat = models.ForeignKey(Listings, on_delete=models.CASCADE,
                                          related_name='conversation_boat')
    conversation_buyer = models.ForeignKey(User, on_delete=models.CASCADE,
                                           related_name='conversation_buyer')
    conversation_seller = models.ForeignKey(User, on_delete=models.CASCADE,
                                            related_name='conversation_seller')
    conversation_thumbnail = models.ImageField(verbose_name='Conversation Image')  # noqa
    last_message_date = models.DateTimeField(verbose_name="Last message date",
                                             blank=True, default=timezone.now)

    class Meta:
        verbose_name = "Conversation"

    def __str__(self):
        return f"{self.conversation_boat}"


class ConversationMessages(models.Model):
    message_conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE, related_name='message_conversation')  # noqa
    message_sent = models.DateTimeField(auto_now=True)
    message_from = models.ForeignKey(User, on_delete=models.CASCADE,
                                     related_name='message_from')  # noqa
    message_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='message_to')
    message_contents = models.CharField(max_length=1000, verbose_name='Message', validators=[MinLengthValidator(1, 'A message cannot be blank.'), MaxLengthValidator(1000)])  # noqa

    class Meta:
        verbose_name = "Conversation Messages"

    def __str__(self):
        return f"{self.message_conversation}"
