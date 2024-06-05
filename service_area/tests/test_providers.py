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
    expected_keys = {'id', 'name', 'email', 'phone_number', 'language', 'currency'}
    assert expected_keys.issubset(response.data.keys())
    assert response.data['name'] == 'New Provider'
    assert response.data['email'] == 'new@example.com'
    assert response.data['phone_number'] == '0987654321'
    assert response.data['language'] == 'en'
    assert response.data['currency'] == 'USD'


@pytest.mark.django_db
def test_get_providers(api_client, create_provider):
    create_provider()
    response = api_client.get('/api/providers/')
    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == 1
    provider = response.data[0]
    expected_keys = {'id', 'name', 'email', 'phone_number', 'language', 'currency'}
    assert expected_keys.issubset(provider.keys())
    assert provider['name'] == 'Test Provider'
    assert provider['email'] == 'test@example.com'
    assert provider['phone_number'] == '1234567890'
    assert provider['language'] == 'en'
    assert provider['currency'] == 'USD'
