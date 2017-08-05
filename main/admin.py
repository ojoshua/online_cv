from django.contrib import admin
from .models import DemoCategory, Demo, Message

admin.site.register(DemoCategory)
admin.site.register(Demo)
admin.site.register(Message)

