from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from bootcamp_m.views import health_check

schema_view = get_schema_view(
    openapi.Info(
        title="bootcamp_m swagger documentation",
        default_version='v1',
        description="bootcamp_m swagger documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="wahtever"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/', include('service_area.urls')),
    path('status/', health_check, name='health_check'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
