from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from service_area.models import Provider, ServiceArea
from service_area.api.serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    @action(detail=False, methods=['get'])
    def locate(self, request):
        lat = float(request.query_params.get('lat'))
        lng = float(request.query_params.get('lng'))
        point = Point(lng, lat)
        service_areas = ServiceArea.objects.filter(geojson__contains=point)
        serializer = self.get_serializer(service_areas, many=True)
        return Response(serializer.data)
