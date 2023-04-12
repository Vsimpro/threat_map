import requests

class Geolocator:
    def __init__(self):
        pass

    def get_location(self, ip):
        ip_address = ip
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        response_json = response.json()

        if response.status_code == 200:
            location_data = (int(response_json.get("latitude")), int(response_json.get("longitude")))
            return location_data

        return False