from rest_framework.routers import DefaultRouter

from api.views import SupplierViewSet, BuyerViewSet


router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'buyer', BuyerViewSet)

urlpatterns = router.urls
