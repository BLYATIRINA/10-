import requests


def find_drugstore(address_ll):

    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = 'cae16195-4dc7-4a5f-b6bb-5164c8eb7440'

    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": ','.join(address_ll),
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    return response.json()
