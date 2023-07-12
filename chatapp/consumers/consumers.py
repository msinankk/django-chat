"""
consumer.py

This module is used to handle websocket requests
"""
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    """
    ChatConsumer
    """

    def connect(self):
        self.accept()
        self.send(json.dumps({"type": "success message"}))
