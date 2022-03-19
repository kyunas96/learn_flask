if __name__ == '__main__':
  import os
  import traceback
  from dotenv import load_dotenv, find_dotenv
  from sqlalchemy import create_engine
  from sqlalchemy.orm import Session
  from sqlalchemyseed import load_entities_from_json, Seeder

  load_dotenv(find_dotenv())
  POSTGRESQL_URI = os.environ.get('POSTGRESQL_URI')
  print(POSTGRESQL_URI)

  engine = create_engine(POSTGRESQL_URI)

  session = Session(engine)
  seeder = Seeder(session)
  entities = load_entities_from_json('./seeds.json')

  try:
    seeder.seed(entities)
    session.commit()
    print('here')
  except Exception as e:
    # print(traceback.format_exc())
    print(f"error: {e}")

  session.close()