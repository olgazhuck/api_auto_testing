from endpoints.authorization import AuthEndpoint
from endpoints.token_alive import TokenAlive


# token tests
def test_authorization_positive(get_token):
    assert get_token, "Token was not generated"


def test_authorization_failsOnEmptyName():
    authEndpoint = AuthEndpoint()
    authEndpoint.get_token_no_validation(name=None)
    assert authEndpoint.response.status_code == 400, "Token was not generated"


def test_authorization_failsOnWrongType():
    authEndpoint = AuthEndpoint()
    authEndpoint.get_token_no_validation(name=1)
    assert authEndpoint.response.status_code == 400, "Token was not generated"


def test_token_is_alive(get_token):
    tokenEndpoint = TokenAlive()
    is_token_alive = tokenEndpoint.is_token_alive(get_token)
    assert is_token_alive is True


def test_token_is_expired():
    tokenEndpoint = TokenAlive()
    is_token_alive = tokenEndpoint.is_token_alive('invalid-token-should-fail')
    assert is_token_alive is False


# get tests
def test_get_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_status_200()


def test_get_one_meme(new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme(new_meme_id)
    get_meme_endpoint.check_status_200()
    assert get_meme_endpoint.json['id'] == new_meme_id


# delete test
def test_delete_meme(new_meme_id, delete_meme_endpoint, get_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_status_200()
    get_meme_endpoint.get_meme(new_meme_id)
    get_meme_endpoint.check_status_404()


# put tests
def test_put_a_post(new_meme_id, update_meme_data, meme_builder):
    updated_meme = meme_builder \
        .create_default_meme(new_meme_id) \
        .with_text("Changed Value") \
        .with_colors(["yellow", "red"]) \
        .build()
    update_meme_data.put_meme(new_meme_id, updated_meme)
    update_meme_data.check_status_200()
    assert update_meme_data.json['text'] == "Changed Value"
    assert update_meme_data.json["info"]["colors"] == ["yellow", "red"]


def test_put_a_post_empty_data(new_meme_id, update_meme_data, meme_builder):
    updated_meme = meme_builder \
        .create_default_meme(new_meme_id) \
        .with_colors("") \
        .with_text("") \
        .with_objects("") \
        .with_url("") \
        .build()
    update_meme_data.put_meme(new_meme_id, updated_meme)
    update_meme_data.check_status_200()
    assert update_meme_data.json["text"] == ""
    assert update_meme_data.json["info"]["colors"] == ""
    assert update_meme_data.json["info"]["objects"] == ""
    assert update_meme_data.json["url"] == ""


def test_updated_by_field_protected(
        new_meme_id, update_meme_data,
        meme_builder):
    updated_meme = meme_builder \
        .create_default_meme(new_meme_id) \
        .with_updated_by("Wane") \
        .build()
    update_meme_data.put_meme(new_meme_id, updated_meme)
    update_meme_data.check_status_200()
    assert update_meme_data.json["updated_by"] == "olga"


# create tests
def test_create_mem_wrong_url(meme_builder, create_meme_endpoint):
    new_meme = meme_builder \
        .create_new_meme() \
        .with_url("dfg") \
        .build()
    create_meme_endpoint.new_meme(new_meme)
    create_meme_endpoint.check_status_200()
    assert create_meme_endpoint.json["url"] == "dfg"


def test_create_empty_mem(meme_builder, create_meme_endpoint):
    new_meme = meme_builder \
        .create_new_meme() \
        .build()
    create_meme_endpoint.new_meme(new_meme)
    create_meme_endpoint.check_status_200()
    assert create_meme_endpoint.json["info"]["colors"] == []
    assert create_meme_endpoint.json["info"]["objects"] == []
    assert create_meme_endpoint.json["tags"] == []
    assert create_meme_endpoint.json["text"] == ""
    assert create_meme_endpoint.json["updated_by"] == "olga"
    assert create_meme_endpoint.json["url"] == ""


def test_create_mem(meme_builder, create_meme_endpoint):
    new_meme = meme_builder \
        .create_new_meme() \
        .with_colors(["purple", "pink"]) \
        .with_text("hello") \
        .with_objects(["rose", "lily"]) \
        .with_url("http:/purple.com") \
        .with_tags(["fun", "flowers"]) \
        .build()
    create_meme_endpoint.new_meme(new_meme)
    create_meme_endpoint.check_status_200()
    assert create_meme_endpoint.json["info"]["colors"] == ["purple", "pink"]
    assert create_meme_endpoint.json["info"]["objects"] == ["rose", "lily"]
    assert create_meme_endpoint.json["tags"] == ["fun", "flowers"]
    assert create_meme_endpoint.json["text"] == "hello"
    assert create_meme_endpoint.json["updated_by"] == "olga"
    assert create_meme_endpoint.json["url"] == "http:/purple.com"
