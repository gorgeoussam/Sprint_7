import allure
import requests
import pytest


class TestOrderMethods:

    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title("creating order with specific color")
    def test_create_order_successful(self, color, order_methods):
        order_data = {
            "firstName": "Syoma",
            "lastName": "Ivanov",
            "address": "SPB, 56",
            "metroStation": 2,
            "phone": "+7 777 777 77 77",
            "rentTime": 5,
            "deliveryDate": "2024-05-20",
            "comment": "no comment",
            "color": color
        }

        with allure.step(f"Create order with color: {color}"):
            response = order_methods.create_order(order_data)
            assert "track" in response.json()

    @allure.title("receiving orders list")
    def test_get_orders_returns_order_list(self, order_methods):
        required_fields = ["id", "firstName", "lastName", "address", "metroStation", "phone",
                           "rentTime", "deliveryDate", "track", "color", "comment", "createdAt",
                           "updatedAt", "status"]

        with allure.step("Send request to retrieve orders"):
            response = order_methods.get_orders()
            orders = response.json().get("orders", [])

        with allure.step("Check presence of required fields"):
            missing_fields = [field for field in required_fields if field not in orders[0]]
            assert not missing_fields