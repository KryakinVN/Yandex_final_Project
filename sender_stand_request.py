# Владимир Крякин, 7-я когорта - Финальный проект. Инженер по тестированию плюс
import configuration as c
import data
import requests

# Создание пользователя и получение авто токена

def post_new_order():
    response = requests.post(c.URL_SERVICE + c.CREATE_USER_ORDER,
                             json=data.order_body,headers=data.headers)
    if response.status_code == 201:
        return response.json()['track']  # Возвращаем в ответе трек номер

track = post_new_order()
print (track)

# Полученияе и сравнение статус кода запроса
def get_order_track(param):
    response = requests.get(c.URL_SERVICE + c.GET_ORDER_TRACK + str(track))
    assert response.status_code == param, f"Статус код ожидаемый '{200}', Получен {response.status_code}"



