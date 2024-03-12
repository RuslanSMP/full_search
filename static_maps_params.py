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
# https://static-maps.yandex.ru/v1?lang=ru_RU&
# pt=28.98624,41.043451~28.95624,41.043451,78~28.94114,41.043451,pmgrs~28.98124,41.043451,pm2rdm~28.97624,41.043451,pmntl100~28.965573,41.04311,pmors23~28.950111,41.043451,flag~28.969573,41.04311,pm2ywl99~37.608,55.6,round&apikey=YOUR_API_KEY
