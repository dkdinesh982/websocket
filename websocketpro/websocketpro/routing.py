# from channels.routing import ProtocolTypeRouter
# from channels.auth import AuthMiddlewareStack
# application = ProtocolTypeRouter({
#     # Empty for now (http->django views is added by default)
# })

from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import websocketapp.routing

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             websocketapp.routing.websocket_urlpatterns
#         )
#     ),
# })
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import websocketapp.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocketapp.routing.websocket_urlpatterns
        )
    ),
})