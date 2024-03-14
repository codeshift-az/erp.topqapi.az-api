from rest_framework.routers import SimpleRouter

from server.apps.order.views import OrderItemViewSet, OrderViewSet

app_name = "orders"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}", OrderViewSet)
router.register(f"{app_name}/items", OrderItemViewSet)

urlpatterns = router.urls
