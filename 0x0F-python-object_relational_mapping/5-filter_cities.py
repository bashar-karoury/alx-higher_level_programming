#!/usr/bin/python3
""" Script to list all states from database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    if ';' not in state_name:
        db = MySQLdb.connect(
                        host="localhost",
                        user=username,
                        passwd=password,
                        db=database
                    )
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM states JOIN cities ON"
                    " states.id = cities.state_id WHERE states.name = '{}'"
                    .format(state_name))
        rows = cur.fetchall()
        for index, row in enumerate(rows):
            print(row[0], end='')
            if (index < len(rows) - 1):
                print(', ', end='')
        print("")

        cur.close()
        db.close()
