import requests
import allure
from api_testing.data import *

class OrderMethods:

    def __init__(self):
        self.base_url = BASE_URL

    @allure.step("Create order")
    def create_order(self, order_data):
        url = CREATE_ORDER_AND_GET_ORDER_LIST
        response = requests.post(url, json=order_data)
        return response

    @allure.step("Get orders")
    def get_orders(self):
        url = CREATE_ORDER_AND_GET_ORDER_LIST
        response = requests.get(url)
        return response

