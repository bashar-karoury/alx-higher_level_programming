#!/usr/bin/python3
""" Script to list all states from database hbtn_0e_0_usa
"""
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
                    host="localhost",
                    user=username,
                    passwd=password,
                    db=database
                )
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(row)