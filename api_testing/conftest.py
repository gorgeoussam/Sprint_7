import pytest
from api_testing.methods.courier_methods import CourierMethods
from api_testing.methods.order_methods import OrderMethods


@pytest.fixture(scope="class")
def courier_methods():
    return CourierMethods()

@pytest.fixture(scope="class")
def order_methods():
    return OrderMethods()