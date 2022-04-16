import json

USER_MODEL_KEYS = [
  "id", "username", "avatar_s3_object_id",
  "email", "session_token", "location", "bio"
  ]

def test_valid_session_login(client):
    res = client.post('/session/login', data={
        "username": "Kevin",
        "password": "password"
    })
    assert res.status_code == 200
    res_json = json.loads(res.data.decode())
    for key in res_json.keys():
      assert key in USER_MODEL_KEYS

def test_invalid_session_login(client):
  res = client.post('/session/login', data={
      "username": "Kevin",
      "password": "incorrect"
  })
  assert res.status_code == 400

def test_valid_session_logout(client):
  res = client.post('/session/login', data={
      "username": "Kevin",
      "password": "password"
  })
  user = json.loads(res.data.decode())
  client.set_cookie('session_token', user['session_token'])
  logoutRes = client.post('/session/logout')
  assert logoutRes.status_code == 204

def test_invalid_session_logout(client):
  logoutRes = client.post('/session/logout')
  assert logoutRes.status_code == 404
