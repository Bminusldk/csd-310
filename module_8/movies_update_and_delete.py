import mysql.connector

def show_films(cursor, message):
    query = "SELECT film_name, film_director, genre_name, studio_name FROM film JOIN studio ON film.studio_id = studio.studio_id JOIN genre ON film.genre_id = genre.genre_id"
    cursor.execute(query)
    print(message)
    for film_name, film_director, genre_name, studio_name in cursor:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film_name, film_director, genre_name, studio_name))

cnx = mysql.connector.connect(user='movies_user', password='popcorn', host='localhost', database='movies', auth_plugin='mysql_native_password')
cursor = cnx.cursor()

# Display all films
show_films(cursor, "-- DISPLAYING FILMS --")

# Insert a new film
insert_film = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('I am Legend', '2007', '120', 'Francis Lawrence', (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'), (SELECT genre_id FROM genre WHERE genre_name = 'Drama'))"
cursor.execute(insert_film)
cnx.commit()

# Display all films
show_films(cursor, "-- DISPLAYING FILMS AFTER INSERTING NEW FILM --")

# Update the film 'Alien' to be a Horror film
update_film = "UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien'"
cursor.execute(update_film)
cnx.commit()

# Display all films
show_films(cursor, "-- DISPLAYING FILMS AFTER UPDATING ALIEN TO BE A HORROR FILM --")

# Delete the film 'Gladiator'
delete_film = "DELETE FROM film WHERE film_name = 'Gladiator'"
cursor.execute(delete_film)
cnx.commit()

# Display all films
show_films(cursor, "-- DISPLAYING FILMS AFTER DELETING GLADIATOR --")

cursor.close()
cnx.close()
