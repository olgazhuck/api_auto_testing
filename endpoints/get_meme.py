import requests
from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):

    def __init__(self, token_id, url='http://167.172.172.115:52355/meme'):
        self.token = token_id
        self.url = url
        self.response = None
        self.json = None

    def get_meme(self, meme_id):
        headers = {'Authorization': self.token}
        self.response = requests.get(f'{self.url}/{meme_id}', headers=headers)
        self.json = self.response.json() if self.response else None
        return self.response

    def get_all_memes(self):
        headers = {'Authorization': self.token}
        self.response = requests.get(self.url, headers=headers)
        self.json = self.response.json() if self.response else None
        return self.response

    def check_status_200(self):
        assert self.response.status_code == 200
