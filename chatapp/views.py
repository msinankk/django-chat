"""
views.py

This module is used to map the methods with the routes
"""
from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Chat project home page method
    """
    return render(request,"index.html")