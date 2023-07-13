from django.contrib import admin
from chatapp.models import ChatRoom, ChatUser

# Register your models here.

admin.site.register([ChatRoom, ChatUser])
