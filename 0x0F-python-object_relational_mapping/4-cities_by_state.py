#!/usr/bin/python3
"""query that shows all cities and are arrenged in ascending order """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    # creation of the database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    # the cursor to be used in te excution of te sql query
    cur = db.cursor()

    # execution of the sql query
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC')

    rows = cur.fetchall()
    for i in rows:
        print(i)

    # close the connection
    cur.close()
    db.close()
