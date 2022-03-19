if __name__ == '__main__':
    from get_db_engine import get_db_engine
    from create_tables import create_tables
    from sqlalchemy.orm import Session
    from sqlalchemyseed import load_entities_from_json, Seeder

    def seed_database():
        seed_users(engine)
        engine = get_db_engine()
        # will create all tables that do not exist for the given models
        create_tables(engine)

    def seed_users(engine):
        # will create database at url if it does not exit

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

    def seed_posts(engine):
        substitute_names_for_ids()

    def substitute_names_for_ids(file, username_dict):
