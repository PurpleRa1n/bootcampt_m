from http import HTTPStatus

from django.contrib.gis.geos import Point
from django.core.cache import cache
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from service_area.api.constants import CACHE_LOCATE_TIMEOUT
from service_area.api.serializers import ProviderSerializer, ServiceAreaSerializer, LocationQueryParamsSerializer
from service_area.models import Provider, ServiceArea


class ProviderViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given provider.

    list:
    Return a list of all the existing providers.

    create:
    Create a new provider.

    delete:
    Remove an existing provider.

    update:
    Update an existing provider.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given service area.

    list:
    Return a list of all the existing service areas.

    create:
    Create a new service area.

    delete:
    Remove an existing service area.

    update:
    Update an existing service area.
    """
    queryset = ServiceArea.objects.select_related('provider')
    serializer_class = ServiceAreaSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'lat',
                openapi.IN_QUERY,
                description="Latitude of the point",
                type=openapi.TYPE_NUMBER,
                required=True
            ),
            openapi.Parameter(
                'lng',
                openapi.IN_QUERY,
                description="Longitude of the point",
                type=openapi.TYPE_NUMBER,
                required=True
            )
        ],
        responses={HTTPStatus.OK: ServiceAreaSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def locate(self, request):
        """
        Locate service areas that contain a given point.
        """
        query_params_serializer = LocationQueryParamsSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        lat = query_params_serializer['lat'].value
        lng = query_params_serializer['lng'].value
        cache_key = f'service_area_{lat}_{lng}'

        cached_result = cache.get(cache_key)
        if cached_result is not None:
            return Response(cached_result)

        point = Point(lng, lat)
        service_areas = ServiceArea.objects.filter(geojson__contains=point)
        serializer = self.get_serializer(service_areas, many=True)
        response_data = serializer.data
        cache.set(cache_key, response_data, timeout=CACHE_LOCATE_TIMEOUT)

        return Response(response_data)
