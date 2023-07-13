"""
methods.py

This module is used to write custom methods to chatapp
"""
from chatapp.models import ChatRoom


def private_room(user1, user2):
    """
    Private room method
    """
    room = ChatRoom()
    room.name = user1.username + user2.username
    room.users.add([user1, user2])
    room.save()
    return room
