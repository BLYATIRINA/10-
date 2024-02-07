import requests
GEOCODER_API_SERVER = 'http://geocode-maps.yandex.ru/1.x/'
GEOCODER_API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def get_toponym_coords(address):
    """

    :rtype: object
    """
    geocoder_params = {
        'apikey': GEOCODER_API_KEY,
        'geocode': address,
        'results': 1,
        'format': 'json'
    }

    response = requests.get(GEOCODER_API_SERVER, params=geocoder_params)
    if not response:
        return ()

    json_response = response.json()
    geo_object = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    return geo_object["Point"]["pos"].split(" ")

