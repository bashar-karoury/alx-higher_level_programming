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
    all_cities = session.query(City).order_by(City.id.asc()).all()
    for city in all_cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
