#!/usr/bin/python3
"""query that shows all cities and are arrenged in ascending order """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC')

    rows = cur.fetchall()
    for i in rows:
        print(i)

    # close the processes
    cur.close()
    db.close()
