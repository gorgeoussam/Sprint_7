import requests
import allure
from api_testing.data import *

class CourierMethods:

    def __init__(self):
        self.base_url = BASE_URL

    @allure.step('create courier')
    def create_courier(self, login, password, first_name):
        url = CREATE_COURIER
        data = {
            "login": login,
            "password": password,
            "first_name": first_name,
        }

        response = requests.post(url, json=data)
        return response

    @allure.step('create courier without password')
    def create_courier_without_password(self, data):
        url = CREATE_COURIER
        response = requests.post(url, json=data)
        return response

    @allure.step('delete courier')
    def delete_courier(self, courier_id):
        url = DELETE_COURIER.format(id=courier_id)
        response = requests.post(url)
        return response

    @allure.step('login existing courier')
    def login_courier(self, login, password):
        url = COURIER_LOGIN
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(url, json=data)
        return response

    @allure.step('login new courier without login')
    def login_courier_without_login(self, password):
        url = COURIER_LOGIN
        data = {
            "password": password
        }
        response = requests.post(url, json=data)
        return response

    @allure.step('login with wrong password fails')
    def login_courier_with_wrong_password(self, login, password):
        url = COURIER_LOGIN
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(url, json=data)
        return response