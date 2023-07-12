"""
views.py

This module is used to map the methods with the routes
"""
from django.shortcuts import render

# Create your views here.


def chat(request):
    """
    Chat project chat page method
    """
    return render(request, "chat.html")
