#!/usr/bin/python3
""" List all state objects using sqlalchemy """

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker
    from model_state import Base, State

    username = 'root'
    password = 'password'
    db_name = 'hbtn_0e_6_usa'
    host = 'localhost'
    port = 3306

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f'{state.id}: {state.name}')
