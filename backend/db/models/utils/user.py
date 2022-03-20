import os, binascii
def create_session_token():
  return binascii.b2a_hex(os.urandom(12))