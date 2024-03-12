import requests


def get_image_maps(address_ll="", delta="0.005"):
    # на всякий случай
    delta = str(delta)
    map_params = {
        "ll": address_ll,
        "pt": f"{address_ll},org",
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    if response:
        return response.content
