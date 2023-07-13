from django.contrib import admin
from chatapp.models import ChatRoom, ChatUsers

# Register your models here.

admin.site.register([ChatRoom, ChatUsers])
