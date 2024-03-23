from rest_framework.routers import SimpleRouter

from server.apps.factory.sale.views import FactorySaleViewSet

app_name = "factory/sales"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}", FactorySaleViewSet)

urlpatterns = router.urls
