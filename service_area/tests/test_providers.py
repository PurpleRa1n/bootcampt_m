from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_create_provider(api_client):
    response = api_client.post('/api/providers/', {
        'name': 'New Provider',
        'email': 'new@example.com',
        'phone_number': '0987654321',
        'language': 'en',
        'currency': 'USD'
    }, format='json')
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_get_providers(api_client, create_provider):
    create_provider()
    response = api_client.get('/api/providers/')
    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == 1
