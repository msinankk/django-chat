"""
methods.py

This module is used to write custom methods to chatapp
"""
import uuid
from urllib.parse import parse_qs
from django.db.models import Count
from chatapp.models import ChatRoom


def private_room(user1: object, user2: object):
    """
    Private room method
    """
    existing_room = ChatRoom.objects.filter(is_private=True).annotate(num_users=Count('users')).filter(num_users=2, users=user1).filter(users=user2)

    if existing_room.exists():
        room = existing_room.first()
        return room
    room = ChatRoom()
    room.name = str(uuid.uuid4())
    room.save()
    room.users.set([user1.id, user2.id])
    return room


def decode_query_string(query_string):
    """
    Query string decode method
    """
    # Parse the query string into a dictionary
    decoded_data = parse_qs(query_string)

    # Process the decoded data as needed
    # ...

    # Return the decoded data
    return decoded_data
