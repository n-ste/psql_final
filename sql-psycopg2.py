import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor obj of the database
cursor = connection.cursor()

# Query 1 - select all the records from the "artist" table
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the "name" column frm the "artist" table
#cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only "Queen" from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - select only by "artist_id" #51 from the "artist" table
cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# fetch the results (multiple)
#results = cursor.fetchall()

# fetch the result (single)
results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)