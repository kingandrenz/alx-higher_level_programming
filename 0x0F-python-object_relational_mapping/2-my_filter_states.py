#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    usr_state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password)
    cur = db.cursor()
    cur.execute("SELECT * FROM states where name = f'{usr_state}' ORDER BY id ASC")

    States = cur.fetchall()


    for state in States:
        print(state)

    cur.close()
    db.close()
