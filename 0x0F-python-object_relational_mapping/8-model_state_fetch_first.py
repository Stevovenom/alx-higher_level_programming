#!/usr/bin/python3

if __name__ == '__main__':

    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker
    from model_state import Base, State

    user = 'root'
    host = 'localhost'
    passwd = 'password'
    port = 3306
    db = 'hbtn_0e_6_usa'
