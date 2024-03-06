from rest_framework.routers import SimpleRouter

from server.apps.warehouse.views import EntryViewSet, ProductViewSet

app_name = "warehouse"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}/entries", EntryViewSet)
router.register(f"{app_name}/products", ProductViewSet)

urlpatterns = router.urls
