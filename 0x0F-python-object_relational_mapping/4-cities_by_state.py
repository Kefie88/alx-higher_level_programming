#!/usr/bin/python3

"""
Lists all cities from the database
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    cont = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], db=argv[3], charset="utf8")
    cursor = cont.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    cont.close()
