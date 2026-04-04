import sqlite3
def init_db():
    with sqlite3.connect("Movies.db") as conn:
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS MOVIES (Title TEXT UNIQUE , Genre TEXT)")

        movies_data = [
            ("Inception", "Sci-Fi"),
            ("Interstellar", "Sci-Fi"),
            ("Avengers", "Action"),
            ("Iron Man", "Action"),
            ("Mad Max: Fury Road", "Action"),
            ("Titanic", "Romance"),
            ("The Notebook", "Romance"),
            ("3 Idiots", "Comedy"),
            ("Hera Pheri", "Comedy"),
            ("The Hangover", "Comedy"),
            ("The Conjuring", "Horror"),
            ("Insidious", "Horror"),
            ("Stree", "Horror")
        ]

        cursor.executemany("INSERT OR IGNORE INTO MOVIES(Title,Genre) VALUES(?,?)",movies_data)
        conn.commit()

if __name__ == "__main__":
    init_db()
 

