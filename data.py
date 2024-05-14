import random

CREATE_RANDOM_COURIER_BOODY = {
    "login": f'Luke{random.randint(100, 999)}',
    "password": f'{random.randint(1000, 9999)}',
    "firstName": "Skywalker"
}

CREATE_COURIER = {
    "login": "Not",
    "password": "qwerty",
    "firstName": "Bad"
}

CREATE_ORDER = [
{
    "firstName": f'Boba{random.randint(100, 999)}',
    "lastName": "Fett",
    "address": "Butyrskiy Val Ulitsa, 32",
    "metroStation": 10,
    "phone": "+7 800 200 06 00",
    "rentTime": 2,
    "deliveryDate": "2024-06-06",
    "comment": "Privet",
    "color": []
},
{
    "firstName": f'Boba{random.randint(100, 999)}',
    "lastName": "Fett",
    "address": "Butyrskiy Val Ulitsa, 33",
    "metroStation": 9,
    "phone": "+7 800 200 06 11",
    "rentTime": 5,
    "deliveryDate": "2024-06-07",
    "comment": "Privet",
    "color": ["BLACK"]
},
{
    "firstName": f'Boba{random.randint(100, 999)}',
    "lastName": "Fett",
    "address": "Butyrskiy Val Ulitsa, 34",
    "metroStation": 9,
    "phone": "+7 800 200 06 10",
    "rentTime": 2,
    "deliveryDate": "2024-07-06",
    "comment": "Privet",
    "color": ["GREY"]
},
{
    "firstName": f'Boba{random.randint(100, 999)}',
    "lastName": "Fett",
    "address": "Butyrskiy Val Ulitsa, 35",
    "metroStation": 6,
    "phone": "+7 800 200 06 10",
    "rentTime": 2,
    "deliveryDate": "2024-07-07",
    "comment": "Privet",
    "color": ["BLACK", "GREY"]
}
]

CREATE_COURIER_409_RESPONSE = "Этот логин уже используется"
CREATE_COURIER_400_RESPONSE = "Недостаточно данных для создания учетной записи"
AUTH_COURIER_400_RESPONSE = "Недостаточно данных для входа"
AUTH_COURIER_404_RESPONSE = "Учетная запись не найдена"
