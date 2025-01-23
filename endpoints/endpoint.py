class Endpoint:

    url = 'http://167.172.172.115:52355/meme'
    response = None
    json = None

    def check_status_404(self):
        assert self.response.status_code == 404

    def check_status_200(self):
        assert self.response.status_code == 200
