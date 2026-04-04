import sqlite3
from movies_db import init_db
init_db()
def add_movie():
    movie = input("Enter movie name : ").strip()
    genre = input("Enter movie genre : ").strip()
    with sqlite3.connect("Movies.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO MOVIES (Title,Genre) VALUES (?,?)",(movie,genre) )
            conn.commit()
            print(f"Movie '{movie}' added.")
        except sqlite3.IntegrityError:
            print("Movie already exists.")


def view_movie():
    with sqlite3.connect("Movies.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Title, Genre FROM MOVIES ")
        result = cursor.fetchall()
        if not result:
            print("No movies found")
            return
        print("\nMovies in Database are: ")
        for title,genre in result:
            print(f"{title} ({genre})")
        print()

def recommend():
    Movie = input("Enter Movie Name : ")
    with sqlite3.connect("Movies.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Genre FROM MOVIES WHERE Lower(Title) = ?",(Movie.lower(),))
        result = cursor.fetchone()
        
        if not result:
            print("Movie not found")
            return
        genre = result[0]
        cursor.execute("SELECT Title FROM MOVIES WHERE Genre = ? AND Lower(Title) != ?",(genre,Movie.lower()))
        Recommendations = cursor.fetchall()

        if not Recommendations:
            print("No Recommendation Found")

        else:
            print("Recommended Movies:")
            for movie in Recommendations:
                print("-",movie[0])
        

def delete_movie():
    Movie = input("Enter Movie Name : ").strip()
    with sqlite3.connect("Movies.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM MOVIES WHERE Lower(Title) = ?",(Movie.lower(),))
        conn.commit()
        if cursor.rowcount == 0:
            print("No Movie found to delete")
        else:
            print("Movie deleted")
       


menu = """
1. Add Movie,
2. View Movies,
3. Recommend Movie,
4. Delete Movie,
5. Exit
"""

while True:
    print(menu)
    choice = input("Enter your choice : ")
    if (choice == "1"):
        add_movie()
    elif(choice == "2"):
        view_movie()
    elif(choice == "3"):
        recommend()
    elif(choice == "4"):
        delete_movie()
    elif(choice == "5"):
        break
    else:
        print("Invalid Choice")

