#!/bin/bash

if ! command -v jq &> /dev/null; then
  echo "jq could not be found, please install jq"
  exit 1
fi

check_success() {
  if [ $? -ne 0 ]; then
    echo "Command failed: $1"
    exit 1
  fi
}

echo "Creating provider..."
PROVIDER_ID=$(curl -s -X POST $API_HOST/api/providers/ \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Provider One",
        "email": "provider.one@example.com",
        "phone_number": "1234567890",
        "language": "en",
        "currency": "USD"
      }' | jq -r '.id')
check_success "Create provider"
echo "Provider created with ID: $PROVIDER_ID"

echo "Retrieving provider..."
curl -s -X GET $API_HOST/api/providers/$PROVIDER_ID/
check_success "Retrieve provider"

echo "Listing all providers..."
curl -s -X GET $API_HOST/api/providers/
check_success "List providers"

echo "Updating provider..."
curl -s -X PUT $API_HOST/api/providers/$PROVIDER_ID/ \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Provider One Updated",
        "email": "provider.one.updated@example.com",
        "phone_number": "0987654321",
        "language": "fr",
        "currency": "EUR"
      }'
check_success "Update provider"

echo "Deleting provider..."
curl -s -X DELETE $API_HOST/api/providers/$PROVIDER_ID/
check_success "Delete provider"

echo "Recreating provider for service area tests..."
PROVIDER_ID=$(curl -s -X POST $API_HOST/api/providers/ \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Provider Two",
        "email": "provider.two@example.com",
        "phone_number": "1234567890",
        "language": "en",
        "currency": "USD"
      }' | jq -r '.id')
check_success "Recreate provider"
echo "Provider recreated with ID: $PROVIDER_ID"

echo "Creating service area..."
SERVICE_AREA_ID=$(curl -s -X POST $API_HOST/api/service_areas/ \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Service Area One",
        "price": 50.0,
        "geojson": {
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
        "provider": '"$PROVIDER_ID"'
      }' | jq -r '.id')
check_success "Create service area"
echo "Service area created with ID: $SERVICE_AREA_ID"

echo "Retrieving service area..."
curl -s -X GET $API_HOST/api/service_areas/$SERVICE_AREA_ID/
check_success "Retrieve service area"

echo "Listing all service areas..."
curl -s -X GET $API_HOST/api/service_areas/
check_success "List service areas"

echo "Updating service area..."
curl -s -X PUT $API_HOST/api/service_areas/$SERVICE_AREA_ID/ \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Service Area One Updated",
        "price": 75.0,
        "geojson": {
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
        "provider": '"$PROVIDER_ID"'
      }'
check_success "Update service area"

echo "Deleting service area..."
curl -s -X DELETE $API_HOST/api/service_areas/$SERVICE_AREA_ID/
check_success "Delete service area"

echo "Recreating service area for locate test..."
SERVICE_AREA_ID=$(curl -s -X POST $API_HOST/api/service_areas/ \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Service Area Two",
        "price": 50.0,
        "geojson": {
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
        "provider": '"$PROVIDER_ID"'
      }' | jq -r '.id')
check_success "Recreate service area"
echo "Service area recreated with ID: $SERVICE_AREA_ID"

echo "Locating service areas..."
curl -s -X GET "$API_HOST/api/service_areas/locate/?lat=0.5&lng=0.5"
check_success "Locate service areas"

echo "E2E tests completed successfully!"
