import data

class ChangeTestData:
    @staticmethod
    def change_data_create_courier(key, value):
        body = data.CREATE_COURIER.copy()
        body[key] = value

        return body

