if __name__ == '__main__':
  import os
  from dotenv import load_dotenv, find_dotenv
  from sqlalchemy import create_engine
  from sqlalchemy_utils import database_exists, create_database

  load_dotenv(find_dotenv())
  POSTGRESQL_URI = os.environ.get('POSTGRESQL_URI')
  
  engine = create_engine(POSTGRESQL_URI)
  if not database_exists(engine.url):
      create_database(engine.url)
      print(f'Database created at {engine.url}\n')
  else:
    print(f'Database at {engine.url} already exists')