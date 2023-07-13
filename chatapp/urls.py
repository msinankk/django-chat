"""
urls.py

This module is used to register the URL routes/path with Python methods
"""
from django.urls import path
from chatapp import views


urlpatterns = [
    path("", views.chat),
    path("previous-chat", views.previous_chat, name="previous-chat"),
]
