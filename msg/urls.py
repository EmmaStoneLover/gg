
from django.contrib import admin
from django.urls import path, include

from msg.models import Message
from .views import *

urlpatterns = [
    path('', msg, name="msg"),
    path('privat', privat, name="privat"),
]
