from rest_framework.routers import SimpleRouter

from server.apps.warehouse.views import WarehouseCartItemViewSet, WarehouseEntryViewSet, WarehouseItemViewSet

app_name = "warehouse"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}/entries", WarehouseEntryViewSet)
router.register(f"{app_name}/items", WarehouseItemViewSet)
router.register(f"{app_name}/cart/items", WarehouseCartItemViewSet)

urlpatterns = router.urls
