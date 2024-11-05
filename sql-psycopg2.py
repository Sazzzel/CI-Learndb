# using the terminal
#import psycopg2

#conect to "chinook" database
#connection = psycopg2.connect(database="chinook")

#build a curser object of the database
#cursor = connection.cursor()

# Query 1 
#cursor.execute('SELECT * FROM "Artist"')

# Query 2
#cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Philip Glass"])

# Query 7
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

#fetch the results (Multi)
#results = cursor.fetchall()

#fetch the results (Single)
#results = cursor.fetchone()

# close connection
#connection.close()

#print results
#for result in results:
    #print(result)


