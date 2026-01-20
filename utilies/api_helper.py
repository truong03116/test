import requests


class APIHelper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'APIHelper/1.0'
        })
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()