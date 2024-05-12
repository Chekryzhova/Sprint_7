import requests
import urls
import allure

class ScooterApi:
    @allure.step('Создаём курьера')
    @staticmethod
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @allure.step('Авторизуемся курьером')
    @staticmethod
    def login_courier(auth_body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=auth_body)

    @allure.step('Создаём заказ')
    @staticmethod
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @allure.step('Получаем список заказов')
    @staticmethod
    def get_order_list():
        return requests.get(urls.BASE_URL + urls.GET_ORDER_LIST_ENDPOINT)