#!/usr/bin/python3
""" Select states with names matching arguments """
import MySQLdb
from sys import argv

# will not execute if the function is imported
if __name__ == "__main__":

    user_state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2],db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT cities.name FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY states.id ASC', (user_state,))

    result = []
    print(', '.join([value[0] for value in cur.fetchall()]))
