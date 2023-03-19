#!/usr/bin/python3
""" This script list all the states from the database using sqlalchemy orm
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
    states = session.query(State.id, State.name).filter(State.name == argv[4])
    states = states.first()
    if states:
        print(states[0])
    else:
        print("Not found")
