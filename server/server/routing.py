from django.urls import path

from .consumers import ChatConsumer

urls_Patterns=[
    path('ws/chat',ChatConsumer.as_asgi(),name="chat")
]