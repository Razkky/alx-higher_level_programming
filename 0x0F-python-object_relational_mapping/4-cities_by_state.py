#!/usr/bin/python3
""" This script lists all the cities in a database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         db=argv[3], passwd=argv[2], user=argv[1])

    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states \
                ON cities.state_id=states.id \
                ORDER BY cities.id ASC")
        cities = cur.fetchall()
    if cities:
        for city in cities:
            print(city)
