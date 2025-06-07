import pytest
import requests
import random
import string

from api_testing.data import DELETE_COURIER, COURIER_LOGIN
from api_testing.methods.courier_methods import CourierMethods
from api_testing.methods.order_methods import OrderMethods


@pytest.fixture(scope="class")
def courier_methods():
    return CourierMethods()

@pytest.fixture(scope="class")
def order_methods():
    return OrderMethods()

@pytest.fixture
def register_new_courier():
    # Method to generate a random string of given length
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:

        yield login, password, first_name

    else:

        yield None, None, None
@pytest.fixture
def delete_courier_after_test():

    courier_id = None
    yield

    if courier_id:
        response = requests.post(DELETE_COURIER.format(id=courier_id))
        assert response.status_code == 200  # Assuming a successful deletion returns 200

@pytest.fixture
def get_courier_id():
    def _get_courier_id(login, password):
        get_id_data = {
            "login": login,
            "password": password
        }
        get_id_response = requests.post(COURIER_LOGIN, json=get_id_data)
        return get_id_response.json().get("id")

    return _get_courier_id