import allure
from scooter_api import ScooterApi

class TestGetOrderList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('Получаем список всех заказов и проверяем, что ответ содержит параметр "orders"')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')
    def test_get_order_list(self):
        get_order_list_request = ScooterApi.get_order_list()

        assert get_order_list_request.status_code == 200 and "orders" in get_order_list_request.json()
