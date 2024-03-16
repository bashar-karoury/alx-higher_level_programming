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
    State.cities = relationship("City", order_by=City.id,
                                back_populates="state")
    Base.metadata.create_all(engine)
    san_fran = session.query(State).filter_by(name='San Francisco').first()
    if san_fran:
        california = State(name='California', cities=[san_fran])
        session.add(california)
    session.commit()
