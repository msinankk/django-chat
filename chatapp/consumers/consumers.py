"""
consumer.py

This module is used to handle websocket requests
"""
import json
from django.contrib.auth.models import User
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from chatapp.methods import decode_query_string, private_room
from chatapp.models import Message, ChatRoom


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

        user1 = User.objects.get(id=user1_id)
        user2 = User.objects.get(id=user2_id[0])
        room = private_room(user1, user2)
        self.room_group_name = room.name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()
        self.send(json.dumps({"type": "success_connection", "room_name": room.name}))

    def receive(self, text_data=None, bytes_data=None):
        super().receive(text_data, bytes_data)
        text_data_json = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "data": text_data_json,
                "room_name": self.room_group_name,
            },
        )

        return

    def chat_message(self, event):
        """
        The method is used to broad cast the method to the channel
        """
        data = event["data"]
        room_name = event["room_name"]
        sender_id = data["sender_id"]
        text_message = data['message']
        user = User.objects.get(id=sender_id)
        room = ChatRoom.objects.get(name=room_name)

        message = Message()
        message.sender = user
        message.chat_room = room
        message.text = text_message
        message.save()

        self.send(
            text_data=json.dumps({"type": "chat", "data": data, "room_name": room_name})
        )
        return

    def disconnect(self, close_code):
        """
        This method is used to disconnect the connection
        """
        # Disconnect the connection
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )
