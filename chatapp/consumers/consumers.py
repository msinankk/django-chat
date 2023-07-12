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
        self.channel_layer = "test"
        self.send(json.dumps({"type": "success message"}))

    def receive(self, text_data=None, bytes_data=None):
        super().receive(text_data, bytes_data)
        text_data_json = json.loads(text_data)
        message = text_data_json["chat"]
        self.send(
            json.dumps(
                {
                    "type": "chat",
                    "message": message,
                }
            )
        )

        return
