"""
views.py

This module is used to map the methods with the routes
"""
import json
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.sessions.backends.db import SessionStore
from chatapp.methods import private_room

# Create your views here.


def chat(request):
    """
    Chat project chat page method
    """
    if not request.user.is_authenticated:
        return redirect("/admin/login")
    session = SessionStore()
    session["data"] = json.dumps(
        serializers.serialize("json", [request.user]),
    )
    session.save()
    users = User.objects.all()

    return render(request, "chat/chats.html", {"users": users})


def previous_chat(request):
    """
    This method is used to render previous chats from the db
    """
    user = request.user
    receiver_id = request.POST["receiver_id"]
    user2 = User.objects.get(id=receiver_id)
    room = private_room(user, user2)
    print("------------")
    print(room)
    print("------------")
    chats = room.message_set.all()
    chats_json = (serializers.serialize("json", chats),)
    print(chats_json)

    return JsonResponse({"message": "success"})
