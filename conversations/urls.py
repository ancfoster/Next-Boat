from . import views
from django.urls import path

urlpatterns = [
    path('messages/', views.ConversationsList.as_view(), name='conversations_list'),
    path('messages/<id>/', views.ConversationMessageList.as_view(), name='conversation_messages'),
]