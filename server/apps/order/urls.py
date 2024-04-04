from rest_framework.routers import SimpleRouter

from server.apps.order.views import OrderCartItemViewSet, OrderExpenseViewSet, OrderItemViewSet, OrderViewSet

app_name = "orders"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}/cart/items", OrderCartItemViewSet)
router.register(f"{app_name}/expenses", OrderExpenseViewSet)
router.register(f"{app_name}/items", OrderItemViewSet)
router.register(f"{app_name}", OrderViewSet)

urlpatterns = router.urls
