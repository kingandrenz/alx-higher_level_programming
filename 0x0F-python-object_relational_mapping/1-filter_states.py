#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,user=username, passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC")
    States = cur.fetchall()

    for state in States:
        print(state)

    db.close()
