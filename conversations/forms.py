from django import forms
from .models import ConversationMessages

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessages
        fields = ['message_contents']

