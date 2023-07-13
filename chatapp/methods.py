"""
methods.py

This module is used to write custom methods to chatapp
"""
import uuid
from urllib.parse import parse_qs
from chatapp.models import ChatRoom


def private_room(user1:int, user2:int):
    """
    Private room method
    """
    existing_room = ChatRoom.objects.filter(
        is_private=True, users__id__in=[user1, user2]
    )
    print("-------------")
    for room in existing_room:
        if room.users.count() == 2:
            return room
    room = ChatRoom()
    room.name = user1 + user2 + str(uuid.uuid1())
    room.save()
    room.users.set([int(user1), int(user2)])
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
