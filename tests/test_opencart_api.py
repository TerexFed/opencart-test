import pytest
import requests

from src.your_models_module import YourPydanticModel
from faker import Faker

fake = Faker()

api_client_url = 'http://localhost/'


def test_add_to_cart_with_exception(api_client):
    product_id = fake.random_number()
    quantity = fake.random_number()

    api_client.base_url = 'http://invalid.example.com'

    with pytest.raises(requests.RequestException):
        api_client.add_to_cart(product_id, quantity)
