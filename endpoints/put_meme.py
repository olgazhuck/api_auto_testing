import requests
from endpoints.endpoint import Endpoint


class PutMeme(Endpoint):

    def __init__(self, token_id, url='http://167.172.172.115:52355/meme'):
        self.token = token_id
        self.url = url
        self.response = None
        self.json = None

    def put_meme(self, meme_id, body):
        headers = {'Authorization': self.token}
        self.response = requests.put(
            f'{self.url}/{meme_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    def check_updated_meme(self, key, expected_value):
        value = self.json['info'].get(key)
        assert value == expected_value

    def check_status_200(self):
        assert self.response.status_code == 200
