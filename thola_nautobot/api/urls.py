"""REST API urls for thola nautobot."""
from nautobot.core.api.routers import OrderedDefaultRouter
from .views import TholaConfigViews, TholaOnboardingViews

router = OrderedDefaultRouter()
router.register("config", TholaConfigViews)
router.register("onboarding", TholaOnboardingViews)

urlpatterns = router.urls
