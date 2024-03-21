from rest_framework.routers import SimpleRouter

from server.apps.factory.storage.views import FactoryStorageItemViewSet

app_name = "factory/storage"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}/items", FactoryStorageItemViewSet)

urlpatterns = router.urls
