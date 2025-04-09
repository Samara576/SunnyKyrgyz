"""
ASGI config for agromarket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import market.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agromarket.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocet": AuthMiddlewareStack(
        URLRouter(
            market.routing.websocket_urlpatterns
        )
    ),
})
