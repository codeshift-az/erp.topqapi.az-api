from rest_framework.routers import SimpleRouter

from server.apps.supplier.views import SupplierViewSet

app_name = "suppliers"

router = SimpleRouter(trailing_slash=True)
router.register(app_name, SupplierViewSet)

urlpatterns = router.urls
