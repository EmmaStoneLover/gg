
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.msg, name="msg"),
    path('<int:id>', views.msg_id, name="msg_id"),
    path('privat', views.privat, name="privat"),
    # path('<int:pk>', views.MsgId.as_view(), name="msg_id"),
]
