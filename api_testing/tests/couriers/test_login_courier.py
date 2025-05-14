import allure
import requests

from api_testing.conftest import courier_methods
from api_testing.helpers import register_new_courier_and_return_login_password

class TestLoginCourier:
    correct_login = 'gorgeoussam'
    correct_password = 'qazwsx123'
    incorrect_login = 'gorgeoussam1'


    @allure.title('testing successful login of existing courier')
    def test_login_courier_returns_200_and_id(self, courier_methods):
        new_courier_info = register_new_courier_and_return_login_password()
        login, password, first_name = new_courier_info[0], new_courier_info[1], new_courier_info[2]

        response = courier_methods.login_courier(login, password)
        assert response.status_code == 200 and "id" in response.json()

    @allure.title('testing login without login fails')
    def test_login_without_login_fails(self, courier_methods):
        new_courier_info = register_new_courier_and_return_login_password()
        login, password, first_name = new_courier_info[0], new_courier_info[1], new_courier_info[2]
        response = courier_methods.login_courier_without_login(password)
        expected_error_message="Недостаточно данных для входа"
        assert response.status_code == 400 and expected_error_message in response.text

    def test_login_with_wrong_password_fails(self, courier_methods):
        response = courier_methods.login_courier(self.incorrect_login, self.correct_password)
        expected_error_message = "Учетная запись не найдена"
        assert response.status_code == 404 and expected_error_message in response.text

    
