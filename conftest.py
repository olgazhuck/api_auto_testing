import pytest
from endpoints.create_meme import CreateMeme
from endpoints.get_meme import GetMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.put_meme import PutMeme
from endpoints.authorization import AuthEndpoint
from helpers.meme_builder import MemeBuilder


@pytest.fixture(scope='session')
def auth_endpoint():
    return AuthEndpoint()


@pytest.fixture(scope='session')
def get_token(auth_endpoint):
    return auth_endpoint.get_token(name="olga")


@pytest.fixture()
def get_meme_endpoint(get_token):
    return GetMeme(get_token)


@pytest.fixture()
def delete_meme_endpoint(get_token):
    return DeleteMeme(get_token)


@pytest.fixture()
def create_meme_endpoint(get_token):
    return CreateMeme(get_token)


@pytest.fixture()
def update_meme_endpoint(get_token):
    return PutMeme(get_token)


@pytest.fixture()
def update_meme_data(get_token):
    return PutMeme(get_token)


@pytest.fixture()
def meme_builder():
    return MemeBuilder()


@pytest.fixture()
def new_meme_id(get_token):
    endpoint = CreateMeme(get_token)
    meme_id = endpoint.defaul_meme()
    yield meme_id
    deleteEndpoint = DeleteMeme(get_token)
    deleteEndpoint.delete_meme(meme_id)
