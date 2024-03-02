from rest_framework.routers import SimpleRouter

from server.apps.branch.views import BranchViewSet

app_name = "branches"

router = SimpleRouter(trailing_slash=True)
router.register(app_name, BranchViewSet)

urlpatterns = router.urls
