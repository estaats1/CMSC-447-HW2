from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

sql = sqlite3.connect("database.db")

sql.execute("DROP TABLE IF EXISTS users;")

sql.execute("CREATE TABLE users (name TEXT NOT NULL, id INTEGER NOT NULL PRIMARY KEY, points INTEGER NOT NULL);")

sql.execute("INSERT INTO users (name, id, points) VALUES ('Steve Smith', 211, 80);")
sql.execute("INSERT INTO users (name, id, points) VALUES ('Jian Wong', 122, 92);")
sql.execute("INSERT INTO users (name, id, points) VALUES ('Chris Peterson', 213, 91);")
sql.execute("INSERT INTO users (name, id, points) VALUES ('Sai Patel', 524, 94);")
sql.execute("INSERT INTO users (name, id, points) VALUES ('Andrew Whitehead', 425, 99);")
sql.execute("INSERT INTO users (name, id, points) VALUES ('Lynn Roberts', 626, 90);")
sql.execute("INSERT INTO users (name, id, points) VALUES ('Robert Sanders', 287, 75);")

@app.route('/')
def home():
    sql = sqlite3.connect("database.db")
    cur = sql.cursor()
    cur.execute("SELECT * FROM users;")
    all_users = cur.fetchall()
    return render_template('/search.html', users=all_users)

@app.route('/search')
def search():
    return render_template('/search.html')

@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('/create.html')