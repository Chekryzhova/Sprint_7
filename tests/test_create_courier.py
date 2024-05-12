import allure
from scooter_api import ScooterApi
import data
import helper
class TestCourierCreate:
    @allure.title('Тест на успешное создание курьера')
    @allure.description('Генерируем рандомные данные для создания курьера и проверяем, что курьер успешно создался')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')
    def test_success_create_courier(self):
        create_courier_requests = ScooterApi.create_courier(data.CREATE_RANDOM_COURIER_BOODY)

        assert create_courier_requests.status_code == 201 and create_courier_requests.json()["ok"] == True

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    @allure.description('Создаём одного курьера, затем создаём второго курьера с таким же набором данных. Проверяем, что во втором случае курьер не создался и текст ошибки: "Этот логин уже используется"')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')

    def test_create_two_similar_courier(self):
        ScooterApi.create_courier(data.CREATE_COURIER)
        create_similar_courier = ScooterApi.create_courier(data.CREATE_COURIER)

        assert create_similar_courier.status_code == 409 and create_similar_courier.json()["message"] == data.CREATE_COURIER_409_RESPONSE

    @allure.title('Проверяем, что если одного из полей нет, запрос возвращает ошибку')
    @allure.description('Создаём курьера без пароля и проверяем,что вернулась ошибка.  Текст ошибки: "Недостаточно данных для создания учетной записи"')
    @allure.link('https://qa-scooter.praktikum-services.ru/docs/#api-Courier-CreateCourier', name='Документация к АПИ')
    def test_create_courier_without_password(self):
        body = helper.ChangeTestData.change_data_create_courier("password", "")
        create_courier_requests = ScooterApi.create_courier(body)

        assert create_courier_requests.status_code == 400 and create_courier_requests.json()["message"] == data.CREATE_COURIER_400_RESPONSE

