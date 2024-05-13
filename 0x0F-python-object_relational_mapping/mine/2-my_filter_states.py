#!/usr/bin/python3
"""
imports the sql database
"""
import MySQLdb
import sys

# This line checks if the script is being run as the main program
# (not imported as a module). if it is, the code below itwill be executed
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database_name> <name>")
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_arg = sys.argv[4]

    # connect to the database
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

