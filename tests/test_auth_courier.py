import allure
from scooter_api import ScooterApi
import data
import helper
import random

class TestAuthCourier:
    @allure.title('Проверка авторизации курьера')
    @allure.description('Создаём курьера и авторизуемся им. Проверяем, что в ответе есть id')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')
    def test_success_auth_courier(self):
        body = helper.ChangeTestData.change_data_create_courier("login", f'Yoda{random.randint(100, 999)}')
        ScooterApi.create_courier(body)
        auth_body = {
                "login": body["login"],
                "password": body["password"]
        }
        auth_courier_requests = ScooterApi.login_courier(auth_body)

        assert auth_courier_requests.status_code == 200 and auth_courier_requests.json()["id"] is not None

    @allure.title('Запрос на авторизацию курьера без логина')
    @allure.description('Создаём курьера, а затем авторизуемся им без логина. проверяем, что вернулась ошибка и текст ошибки: "Недостаточно данных для входа"')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')
    def test_auth_courier_without_login(self):
        body = helper.ChangeTestData.change_data_create_courier("login", f'Yoda{random.randint(100, 999)}')
        ScooterApi.create_courier(body)
        auth_body = {
            "password": body["password"],
            "login": ""
        }
        auth_courier_requests = ScooterApi.login_courier(auth_body)

        assert auth_courier_requests.status_code == 400 and auth_courier_requests.json()["message"] == data.AUTH_COURIER_400_RESPONSE

    @allure.title('Запрос на авторизацию несуществующего курьера')
    @allure.description('Пытаемся авторизоваться несуществующим курьером. Проверяем, что вернулась ошибка и текст ошибки: "Учетная запись не найдена"')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')
    def test_auth_nonexistent_courier(self):
        body = {
        "login": "IAmAlien",
        "password": "qwerty"
    }
        auth_courier_requests = ScooterApi.login_courier(body)

        assert auth_courier_requests.status_code == 404 and auth_courier_requests.json()["message"] == data.AUTH_COURIER_404_RESPONSE

    @allure.title('Запрос на авторизацию курьера с неправильным логином')
    @allure.description('Создаём курьера, а затем пытаемся залогиниться им с неправильным логином. Проверяем, что вернулась ошибка и текст ошибки: "Учетная запись не найдена"')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')
    def test_auth_courier_with_invalid_login(self):
        ScooterApi.create_courier(data.CREATE_COURIER)
        auth_body = {
            "login": data.CREATE_COURIER["login"] + f'{random.randint(100, 999)}',
            "password": data.CREATE_COURIER["password"]
        }
        auth_courier_requests = ScooterApi.login_courier(auth_body)

        assert auth_courier_requests.status_code == 404 and auth_courier_requests.json()["message"] == data.AUTH_COURIER_404_RESPONSE



