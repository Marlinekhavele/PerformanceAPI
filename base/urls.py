from .views import PerformanceViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'performances', PerformanceViewSet, basename='performance')
urlpatterns = router.urls
