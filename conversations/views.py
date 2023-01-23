from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from PIL import Image
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .models import Conversations, ConversationMessages
from listings.models import Listings
from .forms import ConversationMessageForm


# Shows a list of conversation and filters based on logged in user
# class ConversationsList(LoginRequiredMixin, generic.ListView):
#     model = Conversations
#     template_name = 'conversations/conversations.html'
#     def get_queryset(self):
#         return Conversations.objects.filter(conversation_seller=self.request.user)

class ConversationsList(LoginRequiredMixin, generic.ListView):
    model = (Conversations, ConversationMessages)
    template_name = 'conversations/conversations.html'
    def get_queryset(self):
        return Conversations.objects.filter(Q(conversation_seller=self.request.user) | Q(conversation_buyer=self.request.user))


class ConversationMessageList(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        conv_id = self.kwargs['id']
        message_list = ConversationMessages.objects.filter(message_conversation=conv_id)
        conversation = Conversations.objects.get(pk=conv_id)
        conversation_message_form = ConversationMessageForm()
        context = {'message_list':message_list, 'conversation':conversation, 'conversation_message_form':conversation_message_form}
        return render(request, 'conversations/display_conversation.html', context)

    def post(self, request, id, *args, **kwargs):
        print('post')
        id = self.kwargs['id']
        conversation = Conversations.objects.get(pk=id)
        conversation_buyer = conversation.conversation_buyer
        conversation_message_form = ConversationMessageForm(request.POST)
        if conversation_message_form.is_valid():
            print('form valid')
            conversation_message_form.instance.message_conversation = conversation
            conversation_message_form.instance.message_from = request.user
            if request.user == conversation_buyer:
                conversation_message_form.instance.message_to = conversation_seller
            else:
                conversation_message_form.instance.message_to = conversation_buyer
            print('form save')
            form = conversation_message_form.save()
            form.save()
        return redirect('boat_listings')

