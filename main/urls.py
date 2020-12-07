from django.urls import path
from . import views
import os
# from msg.views import

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('account/', views.account, name="account"),
]
