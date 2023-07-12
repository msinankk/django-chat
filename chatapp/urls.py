"""
urls.py

This module is used to register the URL routes/path with Python methods
"""
from django.urls import path
from chatapp import views
from chatapp import routings


urlpatterns = [
    path("",views.chat)
]

urlpatterns += routings.websocket_urlpatterns
