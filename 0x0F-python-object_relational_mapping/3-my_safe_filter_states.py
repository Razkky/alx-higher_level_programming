#!/usr/bin/python3
""" This scripts takes an arguement and lists
    all states from a database
    hbtn_0c_0_usa that matches that state using MySQLdb"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access database to get list of all states
    that contain the searched name
    """

    con = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2], db=argv[3])
    with con.cursor() as curr:
        curr.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {'name': argv[4]})

        states = curr.fetchall()
    if states is not None:
        for state in states:
            print(state)
