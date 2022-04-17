import json
from faker import Faker

fake = Faker()

def test_user_route_post(client):
  user_dict = {
      "username": fake.first_name(),
      "email": fake.ascii_email(),
      "password": "password",
      "location": fake.city(),
      "bio": fake.paragraph(nb_sentences=5),
      "avatar_s3_object_id": fake.domain_name(5),
  }
  res = client.post('/users/', data=user_dict,
                    content_type='multipart/form-data')
  print(json.loads(res.data.decode()))
  assert res.status_code == 201
