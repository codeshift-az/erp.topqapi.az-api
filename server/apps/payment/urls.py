from rest_framework.routers import SimpleRouter

from server.apps.payment.views import PaymentViewSet

app_name = "payments"

router = SimpleRouter(trailing_slash=True)
router.register(app_name, PaymentViewSet)

urlpatterns = router.urls
