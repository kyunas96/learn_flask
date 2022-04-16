from tests.routes.conftest import client


def test_session_login(client):
    # print(client.__dir__())
    res = client.post('/session/login', data={
        "username": "Kevin",
        "password": "password"
    })
    print(res)
