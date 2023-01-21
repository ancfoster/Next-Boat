from django.contrib import admin
from .models import Conversations

# Register your models here.

@admin.register(Conversations)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("conversation_boat", "conversation_buyer", "conversation_seller",)

