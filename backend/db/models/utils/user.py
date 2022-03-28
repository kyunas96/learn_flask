import base64, M2Crypto
def create_session_token():
  return base64.b64encode(M2Crypto.m2.rand_bytes(32)).decode()