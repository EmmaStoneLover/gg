from django.contrib import admin
from msg.models import Message, Comment, Privat

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'picture_file', 'admin_news', 'top', 'date')
    list_display_links = ('id', 'user')
    list_filter = ('date', 'user', 'top', 'admin_news')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'new', 'user', 'text', 'date')
    list_display_links = ('id', 'user')

@admin.register(Privat)
class PrivatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'date')
    list_display_links = ('id', 'user')
