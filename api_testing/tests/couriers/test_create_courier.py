import allure
import requests

from api_testing.conftest import register_new_courier, delete_courier_after_test, get_courier_id
from api_testing.data import COURIER_LOGIN, ERROR_MESSAGE


class TestCreateCourier:


    @allure.title('testing successful courier creation')
    def test_successful_courier_creation(self, courier_methods, register_new_courier, delete_courier_after_test,
                                         get_courier_id):
        new_courier = register_new_courier
        login, password, first_name = new_courier[0][:-1], new_courier[1], new_courier[2]
        response = courier_methods.create_courier(login, password, first_name)
        assert response.status_code == 201 and response.json()["ok"] == True
        courier_id = get_courier_id(login, password)
        delete_response = delete_courier_after_test

    def test_create_duplicate_courier_returns_409(self, courier_methods, register_new_courier,
                                                  delete_courier_after_test, get_courier_id):
        new_courier = register_new_courier
        login, password, first_name = register_new_courier[0][:-1], new_courier[1], new_courier[2]
        response = courier_methods.create_courier(login, password, first_name)
        response2 = courier_methods.create_courier(login, password, first_name)
        assert response2.status_code == 409 and ERROR_MESSAGE in response2.text
        courier_id = get_courier_id(login, password)
        delete_response = delete_courier_after_test

    def test_create_courier_without_required_parameters_returns_400(self, courier_methods):
        payload = {
                  "password": "1234",
                  "firstName": "saske"
                  }
        error_message = "Недостаточно данных для создания учетной записи"
        response = courier_methods.create_courier_without_password(payload)
        assert response.status_code == 400 and error_message in response.text

    # def test_courier_can_login(self, courier_methods):