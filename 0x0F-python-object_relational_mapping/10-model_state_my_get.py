#!/usr/bin/python3
"""list all state objects from database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            mysql_username,
                            mysql_passwd,
                            mysql_db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    state_1 = session.query(State).filter_by(name=state_name).first()
    if (state_1):
        print(state_1.id)
    else:
        print('Not found')
