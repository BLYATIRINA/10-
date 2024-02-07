import requests
from find_drugstore import find_drugstore
from address_coords import get_toponym_coords
from PIL import Image
from geopy.distance import geodesic as gd #Библиотека для расчёта расстояния между точками
from io import BytesIO
import sys


coords = get_toponym_coords(sys.argv[1:]) #В терминал вводится адрес
response_json = find_drugstore(coords)
drugstores_coordinates = []
for i in response_json['features'][0:10]:
    if i['properties']['CompanyMetaData']['Hours']['text'] == 'ежедневно, круглосуточно':
        point = ',pm2gnm'
    elif i['properties']['CompanyMetaData']['Hours']['text'] == '':
        point = ',pm2grm'
    else:
        point = ',pm2rdm'
    drugstores_coordinates.append(','.join(list(map(str, i['geometry']['coordinates']))) + point)
coords = ','.join(coords)
map_params = {
    'l': 'map',
    'pt': f'{"~".join(drugstores_coordinates)}~{coords},flag'
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
        response.content)).show()






