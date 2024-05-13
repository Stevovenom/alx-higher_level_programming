#!/usr/bin/python3
"""query that shows all cities and are arrenged in ascending order """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    search = '{}'.format(argv[4])

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute('SELECT * FROM cities ORDER BY cities.id ASC;', (search))

    rows = cur.fetchall()
    for i in rows:
        print(i)

    # close the processes
    cur.close()
    db.close()
