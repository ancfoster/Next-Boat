from django.contrib import admin
from .models import Conversations, ConversationMessages


@admin.register(Conversations)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("conversation_boat", "conversation_buyer",
                    "conversation_seller",)


@admin.register(ConversationMessages)
class ConversationMessagesAdmin(admin.ModelAdmin):
    list_display = ("message_from", "message_to")
