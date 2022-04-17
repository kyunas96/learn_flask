import json

def test_user_feed(logged_in_client):
  res = logged_in_client.get('/posts/feed/')
  assert len(res.data.decode()) > 0

def test_valid_post_get(client):
  res = client.get('posts/1')
  assert res.status_code == 200
  post_attrs = ["id", "user_id", "name", "s3_object_id", "description", "created_at"]
  res_json = json.loads(res.data.decode())
  for attr in post_attrs:
    assert attr in res_json

def test_invalid_post_get(client):
  res = client.get('posts/200')
  assert res.status_code == 404
  res_json = json.loads(res.data.decode())
  assert 'error' in res_json