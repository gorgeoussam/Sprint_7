import allure
import requests

from api_testing.data import COURIER_LOGIN
from api_testing.helpers import register_new_courier_and_return_login_password

class TestCreateCourier:


    @allure.title('testing successful courier creation')
    def test_successful_courier_creation(self, courier_methods):
        new_courier = register_new_courier_and_return_login_password()
        login, password, first_name = new_courier[0][:-1], new_courier[1], new_courier[2]

        response = courier_methods.create_courier(login, password, first_name)
        assert response.status_code == 201 and response.json()["ok"] == True

        get_id_data = {
            "login": login,
            "password": password
        }
        get_id_response = requests.post(COURIER_LOGIN, json=get_id_data)

        courier_id = get_id_response.json().get("id")

        delete_response = courier_methods.delete_courier(courier_id)

    def test_create_duplicate_courier_returns_409(self, courier_methods):
        new_courier = register_new_courier_and_return_login_password()
        login, password, first_name = register_new_courier_and_return_login_password()

        response = courier_methods.create_courier(login, password, first_name)
        response2 = courier_methods.create_courier(login, password, first_name)
        error_message = "Этот логин уже используется. Попробуйте другой."
        assert response2.status_code == 409 and error_message in response2.text
        get_id_data = {
            "login": login,
            "password": password
        }
        get_id_response = requests.post(COURIER_LOGIN, json=get_id_data)
        courier_id = response.json().get("id")
        delete_response = courier_methods.delete_courier(courier_id)

    def test_create_courier_without_required_parameters_returns_400(self, courier_methods):
        payload = {
                  "password": "1234",
                  "firstName": "saske"
                  }
        error_message = "Недостаточно данных для создания учетной записи"
        response = courier_methods.create_courier_without_password(payload)
        assert response.status_code == 400 and error_message in response.text

    # def test_courier_can_login(self, courier_methods):