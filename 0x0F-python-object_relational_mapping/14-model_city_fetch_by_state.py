#!/usr/bin/python3

"""Lists all city objects from the database"""

from sys import argv
from model_state import State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmake

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    fro city, state in session.query(City, State) \
            .filte(City.state_id == State.id) \
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
