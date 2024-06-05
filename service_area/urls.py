from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service_area.api.views import ProviderViewSet, ServiceAreaViewSet

router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'service_areas', ServiceAreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
