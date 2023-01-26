from django.urls import path
from .views import ChatRoom

urlpatterns = [
    path('',ChatRoom,name="chat")
]
