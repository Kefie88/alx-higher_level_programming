#!/usr/bin/python3

"""
List all cities from the database
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    con = 0
    conect = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], db=argv[3], charset="utf8")
    cursor = conect.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[2] == argv[4]:
            if con > 0:
                print(", ", end="")
            print(row[1], end="")
            con = con + 1
    print()
    cursor.close()
    conect.close()
