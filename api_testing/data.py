# courier handles
BASE_URL = 'https://qa-scooter.praktikum-services.ru'
CREATE_COURIER = BASE_URL + '/api/v1/courier'
COURIER_LOGIN = BASE_URL + '/api/v1/courier/login/'
DELETE_COURIER = BASE_URL + f'/api/v1/courier/:{id}'
GET_COURIER_ORDERS = BASE_URL + f'/api/v1/courier/:{id}/ordersCount'

# order urls
COMPLETE_ORDER = BASE_URL + f'/api/v1/orders/finish/:{id}'
CANCEL_ORDER = BASE_URL + '/api/v1/orders/cancel'
CREATE_ORDER_AND_GET_ORDER_LIST = BASE_URL + '/api/v1/orders'
GET_ORDER_BY_ID = BASE_URL = '/api/v1/orders/track'
ACCEPT_ORDER = BASE_URL + f'/api/v1/orders/accept/:{id}'

GET_ID_DATA = {
            "login": 'login',
            "password": 'password'
        }

ERROR_MESSAGE = "Этот логин уже используется. Попробуйте другой."