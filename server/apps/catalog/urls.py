from rest_framework.routers import SimpleRouter

from server.apps.catalog.views import ProductRecordViewSet

app_name = "catalog"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}/products", ProductRecordViewSet)

urlpatterns = router.urls
