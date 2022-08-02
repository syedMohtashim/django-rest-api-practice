from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from my_product.viewsets import ProductViewSet

router = DefaultRouter()
router.register('product-abc',ProductViewSet, basename = "my_product")
urlpatterns = router.urls
