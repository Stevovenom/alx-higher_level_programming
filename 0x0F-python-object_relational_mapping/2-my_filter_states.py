#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database_name> <name>")
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_arg = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd=password, db="hbtn_0e_0_usa")

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, (name_arg,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

