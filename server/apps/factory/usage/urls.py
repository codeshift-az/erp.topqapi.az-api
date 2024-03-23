from rest_framework.routers import SimpleRouter

from server.apps.factory.usage.views import FactoryUsageViewSet

app_name = "factory/usages"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}", FactoryUsageViewSet)

urlpatterns = router.urls
