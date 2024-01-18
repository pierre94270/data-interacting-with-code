# pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

# => list (rows) of tuples (columns)
def directors_count(db):
    # return the number of directors contained in the database
    db.execute("""
        SELECT COUNT(*)
        FROM directors d 
        """)
    Ndirectors= db.fetchone()
    return Ndirectors[0]

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db.execute("""
        SELECT name
        FROM directors d
        ORDER BY name ASC 
        """)
    L= db.fetchall()
    return [i[0] for i in L ] 
        
"""def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    db.execute(""
        SELECT *
        FROM movies m 
        WHERE  title LIKE "%Love%" 
        order by title ASC 
        "")
    Love_movies = db.fetchall()
    dir=[]
    for i in range(Love_movies):
        dir.append(i[0]) 
    return dir"""

def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = """
        SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title
    """
    my_sql_query = query
    db.execute(my_sql_query)
    results = db.fetchall()
    #liste.append(i[0]) for i in results2d
    return [x[0] for x in results]

def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    my_sql_query = """
    SELECT COUNT(*)
    FROM directors
    WHERE name LIKE ?;
    """
    db.execute(my_sql_query,(f"%{name}%",))
    result = db.fetchone()
    return result[0]


# What are the movies which are longer than a duration, given by a user, sorted in the alphabetical order? Return a list of movie titles.
"""def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = 
        SELECT Count(*)
        FROM directors
        WHERE UPPER(name) LIKE '% name %'
        
    my_sql_query = query
    db.execute(my_sql_query)
    results = db.fetchall()
    #liste.append(i[0]) for i in results2d
    return [x[0] for x in results]
    pass  # YOUR CODE HERE"""

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    my_sql_query = """
    SELECT
    title,
    minutes
    FROM movies
    WHERE title LIKE '%love%'
    ORDER BY title;
    """
    db.execute(my_sql_query)
    results = db.fetchall()
    #liste.append(i[0]) for i in results2
    return [x[0] for x in results]


#print(directors_list(db))
#(love_movies(db))
