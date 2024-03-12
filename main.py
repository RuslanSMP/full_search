import requests
from io import BytesIO
from static_maps_params import get_image_maps
from PIL import Image


def get_map_picture(coords, delta):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = ". . ."
    address_ll = coords

    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": address_ll,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    if not response:
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первую найденную организацию.
    organization = json_response["features"][0]
    # Название организации.
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    # Адрес организации.
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    # Получаем координаты ответа.
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])

    image = get_image_maps(address_ll=org_point, delta=delta)
    Image.open(BytesIO(image)).show()


# UPD. Получите размеры объекта в градусной мере и передайте
# их в параметр spn запроса в StaticAPI - я расценил это как просто передать нужный размер "delta"
# coords = "37.588392,55.734036"
# delta = "0.005"
coords = input()
delta = input()
get_map_picture(coords, delta)
