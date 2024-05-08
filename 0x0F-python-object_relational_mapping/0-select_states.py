#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa
import MySQLdb
from sys import argv
"""
This condition ensures that the code block beneath it is only executed,
if the script is run directly and not imported as a module into another script
"""
if __name__ == '__main__':

# creating a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
            passwd="password", db="hbtn_0e_0_usa")
# the cursor function that will be used to execute sql queries
    cur=db.cursor()
# executes the query that selects all from states
    cur.execute("SELECT * FROM states")
# fetches the rows from the states column
    rows=cur.fetchall()
# displays the fetched rows
    for row in rows:
        print(row)
# end the proceses
    cur.close()
    db.close()
