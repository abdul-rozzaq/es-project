

from django.urls import path
from .consumers import EchoConsumer

websocket_urlpatterns = [
    path('echo/', EchoConsumer.as_asgi())
]



