from rest_framework.routers import SimpleRouter

from server.apps.staff.views import DriverViewSet, SellerViewSet, WorkerViewSet

app_name = "staff"

router = SimpleRouter(trailing_slash=True)
router.register(f"{app_name}/drivers", DriverViewSet)
router.register(f"{app_name}/sellers", SellerViewSet)
router.register(f"{app_name}/workers", WorkerViewSet)

urlpatterns = router.urls
