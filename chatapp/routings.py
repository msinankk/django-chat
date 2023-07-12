"""
routings.py

This module is used to handle websocket requests
"""

from django.urls import re_path

from chatapp.consumers.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
]
