from django.urls import path
from .consumers import JokesConsumer


ws_urlpatterns = [
    path('ws/web/', JokesConsumer.as_asgi())
]