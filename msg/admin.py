from django.contrib import admin
from msg.models import Message, Comment, Privat

# Register your models here.

admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Privat)
