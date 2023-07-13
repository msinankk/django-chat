"""
models.py

This module is used to register models for the chatapp
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChatUser(models.Model):
    """
    ChatUser model
    """

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=False)


class TrackingModel(models.Model):
    """
    TrackingModel model class
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class to add additional options
        """

        abstract = True


class ChatRoom(TrackingModel):
    """
    ChatRoom model
    """

    name = models.CharField(max_length=50, null=True, blank=True)
    users = models.ManyToManyField(User)
    unread_by_1 = models.PositiveIntegerField(default=0)
    unread_by_2 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.name)


class Message(TrackingModel):
    """
    Message model
    """

    sender = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    file = models.FileField(null=True,blank=True,upload_to="media/")
    is_read = models.BooleanField(default=False)
