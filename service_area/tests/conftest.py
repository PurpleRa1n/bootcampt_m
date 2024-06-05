import pytest
from rest_framework.test import APIClient
from django.contrib.gis.geos import Polygon
from service_area.models import Provider, ServiceArea


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_provider():
    def _create_provider(name='Test Provider', email='test@example.com', phone_number='1234567890', language='en',
                         currency='USD'):
        return Provider.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            language=language,
            currency=currency
        )

    return _create_provider


@pytest.fixture
def create_service_area(create_provider):
    def _create_service_area(name='Test Area', price=100.0, geojson=Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))):
        provider = create_provider()
        return ServiceArea.objects.create(
            name=name,
            price=price,
            geojson=geojson,
            provider=provider
        )

    return _create_service_area
