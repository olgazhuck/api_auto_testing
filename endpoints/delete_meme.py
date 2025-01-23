import requests
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    def __init__(self, token_id, url='http://167.172.172.115:52355/meme'):
        self.token = token_id
        self.url = url
        self.response = None
        self.json = None

    def delete_meme(self, meme_id):
        headers = {'Authorization': self.token}
        self.response = requests.delete(
            f'{self.url}/{meme_id}', headers=headers
        )
        return self.response
