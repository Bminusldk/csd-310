import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="movies_user",
    password="popcorn",
    database="movies",
    auth_plugin='mysql_native_password'
)
# Create a cursor object
cursor = db.cursor()

# First query to select all fields from the studio table
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
print("\n-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# Second query to select all fields from the genre table
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("\n--DISPLAYING Genres RECORDS--")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# Third query to select movie names with runtime less than 2 hours
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
movies = cursor.fetchall()
print("\n--DISPLAYING Short Film RECORDS--")
for movie in movies:
    print("Film Name: {}\nRuntime: {}\n".format(movie[0], movie[1]))

# Fourth query to select film names and directors ordered by director
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
films = cursor.fetchall()
print("\n--Displaying Director RECORDS in Order--")
for film in films:
    print("Name: {}\nDirector: {}\n".format(film[0], film[1]))

# Closing the cursor and the database connection
cursor.close()
db.close()
