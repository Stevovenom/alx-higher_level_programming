#!/usr/bin/python3

import MySQLdb
import sys

"""
check if the script is being runned in the main program and its not imported
as a module, then the script below it, or following willl be executed
"""
if __name__ == '__main__':
    # checksk if the number of scripts passed is not equal to 4
    # if not not, it prints a usage message an dexits with 1
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <username> <password> <database_name>")
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # creating the connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
            passwd="password", db="hbtn_0e_0_usa")

    # creation of the cursor which will be used to execute the swl queries
    cur = db.cursor()
    cur.execute("SELECT DISTINCT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows =  cur.fetchall()
    printed_states = set()

    for row in rows:
        state_id, state_name = row
        if state_name not in printed_states:
            print(row)
            printed_states.add(state_name)

    # clean up the process
    cur.close()
    db.close()
