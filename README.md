# 🎬 Movie Recommendation System (SQLite + Python)

## 📌 Project Overview

This is a simple **command-line based movie management and recommendation system** built using Python and SQLite
It allows users to add movies view stored movies get recommendations based on genre and delete movies from the database

---

## 🎯 Features

* Add new movies with genre
* View all movies in the database
* Get movie recommendations based on genre
* Delete movies from database
* Simple menu-driven interface

---

## 🗄️ Database

* SQLite database used
* Database name: `Movies.db`
* Table: `MOVIES`

### Table Structure

* Title
* Genre

---

## 🛠️ Technologies Used

* Python
* SQLite (`sqlite3`)

---

## ⚙️ How It Works

### 🔹 Add Movie

User enters movie name and genre
Movie is stored in database
Duplicate entries are handled using exception

### 🔹 View Movies

Displays all movies with their genres

### 🔹 Recommend Movie

* User enters a movie name
* System finds its genre
* Recommends other movies from the same genre

### 🔹 Delete Movie

Deletes movie from database using movie name

---

## 🚀 How to Run

```bash id="1n6t3r"
python app.py
```

---

## 📁 Project Structure

```id="e8k5d3"
movie-recommendation-system/
│── app.py
│── movies_db.py
│── README.md
```

---

## 🧠 Example Menu

```id="8rj9v2"
1 Add Movie
2 View Movies
3 Recommend Movie
4 Delete Movie
5 Exit
```

---

## 📌 Key Concepts Used

* SQLite database connection
* CRUD operations
* Exception handling
* User input handling
* Menu-driven programming

---

## 🙌 Author

Prachi Giri Goswami

