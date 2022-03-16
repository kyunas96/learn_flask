if __name__ == '__main__':
  import os
  from dotenv import load_dotenv, find_dotenv
  from sqlalchemy import create_engine
  from sqlalchemy_utils import database_exists, drop_database

  load_dotenv(find_dotenv())
  POSTGRESQL_URI = os.environ.get('POSTGRESQL_URI')
  
  engine = create_engine(POSTGRESQL_URI)
  if database_exists(engine.url):
    drop_database(engine.url)
    print(f'Database at {engine.url} deleted\n')
  else:
    print(f'Database at {engine.url} does not exist\n')