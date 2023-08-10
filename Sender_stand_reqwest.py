
import configuration as c
import data
import requests as requests

# Создание пользователя и получение авто токена

def post_new_order():
    response = requests.post(c.URL_SERVICE + c.CREATE_USER_ORDER,
                             json=data.order_body,headers=data.headers)
    if response.status_code == 201:
        return response.json()['track']  # Возвращаем в ответе трек номер

track = post_new_order()
#print (track)


def get_order_track(track):
    response = requests.get(c.URL_SERVICE + c.GET_ORDER_TRACK + str(track))
    return response.status_code
    code=get_order_track()
    assert code == track


 # if response.status_code == 200:
    #     return "OK"
    # else:
    #     return "Some troble"


