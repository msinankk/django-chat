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
        self.room_group_name = "test"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()
        self.send(json.dumps({"type": "success message"}))

    def receive(self, text_data=None, bytes_data=None):
        super().receive(text_data, bytes_data)
        text_data_json = json.loads(text_data)
        message = text_data_json["chat"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
            },
        )

        return

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"type": "chat", "message": message}))
        return
