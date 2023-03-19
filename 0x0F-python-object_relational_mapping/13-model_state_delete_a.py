#!/usr/bin/python3
"""
    This scripts deletes all states that contain 'a'
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
    states = session.query(State)
    states = states.filter(State.name.contains('a'))
    states = states.order_by(State.id)
    for state in states:
        session.delete(state)
    session.commit()
