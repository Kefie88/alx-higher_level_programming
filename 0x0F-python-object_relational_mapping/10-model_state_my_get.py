#!/usr/bin/python3

"""Prints the State object with the name passed
as argument from the DB
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ =="__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    found = 0
    for state in result:
        if state.name == argv[4]:
            print("{}".format(state.id))
            found = 1
            break
    if found == 0:
        print("Not found")
