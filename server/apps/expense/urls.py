from rest_framework.routers import SimpleRouter

from server.apps.expense.views import ExpenseViewSet

app_name = "expenses"

router = SimpleRouter(trailing_slash=True)
router.register(app_name, ExpenseViewSet)

urlpatterns = router.urls
