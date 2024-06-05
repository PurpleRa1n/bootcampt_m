from http import HTTPStatus

from django.contrib.gis.geos import Point
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from service_area.api.serializers import ProviderSerializer, ServiceAreaSerializer
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
    queryset = ServiceArea.objects.all()
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
        lat = float(request.query_params.get('lat'))
        lng = float(request.query_params.get('lng'))
        point = Point(lng, lat)
        service_areas = ServiceArea.objects.filter(geojson__contains=point)
        serializer = self.get_serializer(service_areas, many=True)
        return Response(serializer.data)
