from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_create_service_area(api_client, create_provider):
    provider = create_provider()
    payload = {
        'name': 'New Area',
        'price': 50.0,
        'geojson': {
            "type": "Polygon",
            "coordinates": [
                [
                    [0, 0],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [0, 0]
                ]
            ]
        },
        'provider': provider.id
    }
    response = api_client.post('/api/service_areas/', payload, format='json')
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_get_service_areas(api_client, create_service_area):
    create_service_area()
    response = api_client.get('/api/service_areas/')
    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_locate_service_area(api_client, create_service_area):
    create_service_area()
    response = api_client.get('/api/service_areas/locate/', {'lat': 0.5, 'lng': 0.5})
    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == 1
