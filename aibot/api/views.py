from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation
from .serializers import ConversationSerializer
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated




class ConversationView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        user = request.user
        uuid = request.query_params.get('uuid')
        
        # If uuid is not provided, return only uuid and conversation_title for the user's conversations
        if not uuid:
            conversations = Conversation.objects.filter(user=user).values('uuid', 'conversation_title')
            return Response(conversations, status=status.HTTP_200_OK)

        # If uuid is provided, return the entire conversation details
        conversation = get_object_or_404(Conversation, user=user, uuid=uuid)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new conversation
        data = request.data
        data['user'] = request.user.id  # Set the user as the current logged-in user
        serializer = ConversationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # Update an existing conversation by adding to conversation_list
        uuid = request.data.get('uuid')
        if not uuid:
            return Response({'error': 'UUID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the conversation and ensure it belongs to the user
        conversation = get_object_or_404(Conversation, user=request.user, uuid=uuid)

        # Extract the new content for conversation_list and add it to the existing list
        new_conversation_part = request.data.get('conversation_list', [])
        if not isinstance(new_conversation_part, list):
            return Response({'error': 'conversation_list must be a list'}, status=status.HTTP_400_BAD_REQUEST)

        # Update conversation_list by appending the new content
        conversation.conversation_list.extend(new_conversation_part)
        conversation.save()

        # Return the updated conversation data
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)

