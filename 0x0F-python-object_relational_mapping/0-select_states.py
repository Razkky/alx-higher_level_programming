#!/usr/bin/python3
""" This scripts lists all states from a database
    hbtn_0c_0_usa using MySQLdb"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access database to get list of all states
    """

    con = MySQLdb.connect(host="localhost", port=3306,
                          user=argv[1], passwd=argv[2], db=argv[3])
    curr = con.cursor()
    curr.execute("SELECT * FROM states")
    states = curr.fetchall()

    for state in states:
        print(state)
