#!/usr/bin/python3
"""
Takes argumnet and displays all values in the states table of our database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    search ='{}'.format(argv[4])

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute('SELECT id, name FROM states WHERE name = %s\
            ORDER BY states.id ASC;', (search,))

    rows = cur.fetchall()
    for i in rows:
        print(i)
