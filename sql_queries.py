# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays

    (songplay_id int PRIMARY KEY, 

    start_time date REFERENCES time(start_time), 

    user_id int REFERENCES users(user_id), 

    level text, 

    song_id text REFERENCES songs(song_id), 

    artist_id text REFERENCES artists(artist_id), 

    session_id int, 

    location text, 

    user_agent text)
""")

user_table_create = ("""   CREATE TABLE IF NOT EXISTS users

    (user_id int PRIMARY KEY, 

    first_name text NOT NULL, 

    last_name text NOT NULL, 

    gender text, 

    level text)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs

    (artist_id text, 
    
    duration float,
    
    song_id text PRIMARY KEY, 

    title text NOT NULL, 
    
    year int)
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists

    (artist_id text PRIMARY KEY,

     lattitude float, 
     
     location text, 

     longitude float,
     
     name text NOT NULL)
""")


time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time

    (start_time date PRIMARY KEY,

     hour int, 

     day int, 

     week int, 

     month int, 

     year int, 

     weekday text)
""")



# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays

    (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    
    ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users

    (user_id, first_name, last_name, gender, level)

    VALUES (%s, %s, %s, %s, %s)
    
    ON CONFLICT (user_id) DO UPDATE SET 
  user_id=EXCLUDED.user_id, first_name=EXCLUDED.first_name,
  last_name=EXCLUDED.last_name, gender=EXCLUDED.gender,level=EXCLUDED.level;    
""")

song_table_insert = ("""INSERT INTO songs

    (song_id, title, artist_id, year, duration)
    
    VALUES (%s, %s, %s, %s, %s)
    
    ON CONFLICT (song_id) DO NOTHING;
 """)

artist_table_insert = ("""INSERT INTO artists

    (artist_id, lattitude, location, longitude, name)

    VALUES (%s, %s, %s, %s, %s)
    
    ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_insert = ("""INSERT INTO time

    (start_time, hour, day, week,month,year,weekday)

    VALUES (%s, %s, %s, %s, %s,%s, %s)
    
    ON CONFLICT (start_time) DO NOTHING;
""")




# FIND SONGS

song_select = ("""
    SELECT song_id, artists.artist_id

    FROM songs JOIN artists ON songs.artist_id = artists.artist_id

    WHERE songs.title = %s

    AND artists.name = %s

    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [time_table_create,user_table_create,artist_table_create,song_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop,time_table_drop]