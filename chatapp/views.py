"""
views.py

This module is used to map the methods with the routes
"""
import json
from django.shortcuts import render
from django.core import serializers
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.


def chat(request):
    """
    Chat project chat page method
    """
    session = SessionStore()
    session["data"] = json.dumps(
        serializers.serialize("json", [request.user]),
    )
    session.save()

    return render(request, "chat/chats.html")
