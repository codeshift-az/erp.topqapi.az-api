from rest_framework.routers import SimpleRouter

from server.apps.factory.product.views import FactoryProductViewSet

app_name = "factory/products"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}", FactoryProductViewSet)

urlpatterns = router.urls
