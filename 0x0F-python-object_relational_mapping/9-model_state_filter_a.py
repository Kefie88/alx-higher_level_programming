#!/usr/bin/python3

"""Lists all State objects from database contain 'a'"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    data = session.query(State).order_by(State.id).filter(State.name.like("%a%")).all()

    for row in data:
        print("{}: {}".format(row.id, row.name))
    session.close()
