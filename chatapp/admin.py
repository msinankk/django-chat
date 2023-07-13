from django.contrib import admin
from chatapp.models import ChatRoom, ChatUser, Message

# Register your models here.

admin.site.register([ChatRoom, ChatUser, Message])
