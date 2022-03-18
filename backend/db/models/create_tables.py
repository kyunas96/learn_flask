from gettext import find
from venv import create

from click import echo


if __name__ == '__main__':
  import os
  from base import Base
  from sqlalchemy import create_engine
  from dotenv import load_dotenv, find_dotenv

  load_dotenv(find_dotenv())

  POSTGRESQL_URI = os.environ.get('POSTGRESQL_URI')

  engine = create_engine(POSTGRESQL_URI, echo=True)



