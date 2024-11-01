from rest_framework import serializers
from .models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['uuid', 'user', 'conversation_title', 'conversation_list', 'date_added']
        read_only_fields = ['uuid', 'date_added']
