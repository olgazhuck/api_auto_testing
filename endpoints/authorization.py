import requests


class AuthEndpoint:

    def __init__(self):
        self.url = 'http://167.172.172.115:52355/authorize'
        self.response = None
        self.json = None

    def get_token_no_validation(self, name):
        body = {"name": name}
        self.response = requests.post(self.url, json=body)
        return

    def get_token(self, name):
        self.get_token_no_validation(name)
        self.check_status_200()
        self.json = self.response.json()
        self.check_token_exists()
        return self.json['token']

    def get_token_from_response(self):
        return self.json['token']

    def is_token_valid(self):
        url = f'{self.url}/{self.get_token_from_response()}'
        self.response = requests.get(url)
        self.json = self.response.json()
        self.check_status_200()
        return self.response.status_code == 200

    def check_status_200(self):
        assert self.response.status_code == 200, (
            f"Expected status 200, but got {self.response.status_code}"
        )

    def check_token_exists(self):
        assert 'token' in self.json, "Token was not found in the response"
