#!/usr/bin/python3

"""Lists al States objects from the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()
    state = session.query(State).first()
    if state is None:
        print("Nothing")
    print('{}: {}'.format(state.id, state.name))
    session.close()
