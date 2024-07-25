import pytest
from fastapi.testclient import TestClient
from main import app
from models.order import Order

client = TestClient(app)

# Test data
valid_order_data = {
    "id": "A0000001",
    "name": "Melody Holiday Inn",
    "address": {
        "city": "taipei-city",
        "district": "da-an-district",
        "street": "fuxing-south-road"
    },
    "price": "1500",
    "currency": "TWD"
}

invalid_order_data_non_english_name = {
    "id": "A0000001",
    "name": "Mélody Holiday Inn",
    "address": {
        "city": "taipei-city",
        "district": "da-an-district",
        "street": "fuxing-south-road"
    },
    "price": "1500",
    "currency": "TWD"
}

invalid_order_data_name_not_capitalized = {
    "id": "A0000001",
    "name": "melody Holiday Inn",
    "address": {
        "city": "taipei-city",
        "district": "da-an-district",
        "street": "fuxing-south-road"
    },
    "price": "1500",
    "currency": "TWD"
}

invalid_order_data_price_over_2000 = {
    "id": "A0000001",
    "name": "Melody Holiday Inn",
    "address": {
        "city": "taipei-city",
        "district": "da-an-district",
        "street": "fuxing-south-road"
    },
    "price": "2500",
    "currency": "TWD"
}

invalid_order_data_invalid_currency = {
    "id": "A0000001",
    "name": "Melody Holiday Inn",
    "address": {
        "city": "taipei-city",
        "district": "da-an-district",
        "street": "fuxing-south-road"
    },
    "price": "1500",
    "currency": "ABC"
}

# Test cases
def test_create_order_success():
    response = client.post("/api/orders", json=valid_order_data)
    assert response.status_code == 200
    assert response.json() == valid_order_data

def test_create_order_fail_non_english_name():
    response = client.post("api/orders", json=invalid_order_data_non_english_name)
    assert response.status_code == 400
    assert response.json()["detail"] == "Name contains Non-English characters"

def test_create_order_fail_name_not_capitalized():
    response = client.post("api/orders", json=invalid_order_data_name_not_capitalized)
    assert response.status_code == 400
    assert response.json()["detail"] == "Name is not Capitalized"

def test_create_order_fail_price_over_2000():
    response = client.post("api/orders", json=invalid_order_data_price_over_2000)
    assert response.status_code == 400
    assert response.json()["detail"] == "Price is over 2000"

def test_create_order_fail_invalid_currency():
    response = client.post("api/orders", json=invalid_order_data_invalid_currency)
    assert response.status_code == 400
    assert response.json()["detail"] == "Currency format is wrong"

