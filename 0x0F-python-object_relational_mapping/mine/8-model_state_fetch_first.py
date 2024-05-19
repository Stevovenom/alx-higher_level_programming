#!/usr/bin/python3

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker
    from model_state import Base, State

    user = 'root'
    host = 'localhost'
    passwd = 'password'
    port = 3306
    db_name = 'hbtn_0e_6_usa'

    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}:{port}/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).first()
    if result:
        print('{}: {}'.format(result.id, result.name))
    else:
        print('Nothing')
