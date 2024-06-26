#!/usr/bin/python3
""" List all state objects using sqlalchemy """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker
    from model_state import Base,State

    user = '{}'.format(argv[1])
    passwd = '{}'.format(argv[2])
    db = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
