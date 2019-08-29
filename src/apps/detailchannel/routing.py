from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import ConsumerComment


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                path('detail/<int:pk>/', ConsumerComment),
            ]
        )
    ),
})


#
# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
# })
