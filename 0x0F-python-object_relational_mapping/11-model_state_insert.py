#!/usr/bin/python3
"""
    This script add a new State to the state table
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    Louisiana = State(name = 'Louisiana')
    session.add(Louisiana)
    session.commit()
    print(Louisiana.id)
