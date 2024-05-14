import allure
import pytest
import data
from scooter_api import ScooterApi



class TestCreateOrder:

    @allure.title('Проверка создания заказа')
    @allure.description('Создаём заказ с разными значениями параметра color в теле запроса. Проверяем, что заказ создался и ответ содержить параметр "track"')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')
    @pytest.mark.parametrize("order", data.CREATE_ORDER)
    def test_create_order(self, order):
        create_order_request = ScooterApi.create_order(order)

        assert create_order_request.status_code == 201 and "track" in create_order_request.json()




