"""
consumer.py

This module is used to handle websocket requests
"""
import json
from django.contrib.auth.models import User
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from chatapp.methods import decode_query_string, private_room


class ChatConsumer(WebsocketConsumer):
    """
    ChatConsumer
    """

    def connect(self):
        session = self.scope["session"]
        data = self.scope["query_string"].decode("utf-8")
        user1_id = session["_auth_user_id"]
        data = decode_query_string(data)
        user2_id = data["user_id"]

        room = private_room(user1_id,user2_id)
        print("----------------")
        print(room)
        print("----------------")
        self.room_group_name = room.name

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
