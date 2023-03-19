#!/usr/bin/python3
""" This script lists all the cities in a database
    in a particular state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         db=argv[3], passwd=argv[2], user=argv[1])

    with db.cursor() as cur:
        cur.execute("SELECT cities.name \
                FROM cities \
                JOIN states \
                ON state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (argv[4],))
        cities = cur.fetchall()
    if cities:
        print(", ".join([city[0] for city in cities]))
