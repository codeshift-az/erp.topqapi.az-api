from rest_framework.routers import SimpleRouter

from server.apps.catalog.views import CatalogItemViewSet

app_name = "catalog"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}/items", CatalogItemViewSet)

urlpatterns = router.urls
