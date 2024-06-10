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
    expected_keys = {'id', 'name', 'price', 'geojson', 'provider'}
    assert expected_keys.issubset(response.data.keys())
    assert response.data['name'] == 'New Area'
    assert response.data['price'] == 50.0
    assert response.data['geojson']['type'] == 'Polygon'
    assert response.data['provider'] == provider.id


@pytest.mark.django_db
def test_get_service_areas(api_client, create_service_area):
    create_service_area()
    response = api_client.get('/api/service_areas/')
    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == 1
    service_area = response.data[0]
    expected_keys = {'id', 'name', 'price', 'geojson', 'provider'}
    assert expected_keys.issubset(service_area.keys())
    assert service_area['name'] == 'Test Area'
    assert service_area['price'] == 100.0
    assert service_area['geojson']['type'] == 'Polygon'
    assert service_area['provider'] == service_area['provider']


@pytest.mark.django_db
def test_locate_service_area(api_client, create_service_area):
    create_service_area()
    response = api_client.get('/api/service_areas/locate/', {'lat': 0.5, 'lng': 0.5})
    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == 1
    service_area = response.data[0]
    expected_keys = {'id', 'name', 'price', 'geojson', 'provider'}
    assert expected_keys.issubset(service_area.keys())
    assert service_area['name'] == 'Test Area'
    assert service_area['price'] == 100.0
    assert service_area['geojson']['type'] == 'Polygon'
    assert service_area['provider'] == service_area['provider']


@pytest.mark.django_db
def test_locate_service_area_empty_params(api_client, create_service_area):
    create_service_area()
    response = api_client.get('/api/service_areas/locate/')
    assert response.status_code == HTTPStatus.BAD_REQUEST
