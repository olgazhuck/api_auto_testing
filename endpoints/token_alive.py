import requests


class TokenAlive:
    def __init__(self):
        self.url = 'http://167.172.172.115:52355/authorize'
        self.response = None
        self.token_alive = False

    def is_token_alive(self, token):
        url = f'{self.url}/{token}'
        self.response = requests.get(url)
        self.token_alive = self.response.status_code == 200
        return self.token_alive
