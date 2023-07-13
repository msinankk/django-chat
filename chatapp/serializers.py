"""
serializers.py

This module is used to write serializer class to chat app
"""
from rest_framework.serializers import Serializer
from chatapp.models import Message


class MessageSerializer(Serializer):
    """
    Serializer class for Message model
    """

    class meta:
        """
        class Meta for additional options
        """

        model = Message
        fields = ["id", "sender", "text", "file", "is_read"]
