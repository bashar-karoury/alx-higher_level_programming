#!/usr/bin/python3
"""list all state objects from database
"""
import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            mysql_username,
                            mysql_passwd,
                            mysql_db_name))

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    california = State(name='California')
    all_states = session.query(State).order_by(State.id.asc()).all()
    for state in all_states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
        """state_cities = session.query(City).order_by(
                            City.id.asc()).filter_by(state=state)
        for city in state_cities:
            print("\t{}: {}".format(city.id, city.name))"""
