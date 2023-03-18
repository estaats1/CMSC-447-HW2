from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

sql = sqlite3.connect("database.db")

with open('schema.sql') as f:
    sql.executescript(f.read())

cur = sql.cursor()

@app.route('/')
def home():
    sql = sqlite3.connect("database.db")
    cur = sql.cursor()
    cur.execute("SELECT * FROM users;")
    all_users = cur.fetchall()
    return render_template('/home.html', users=all_users)

@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        user = request.form['search_user']
        sql = sqlite3.connect("database.db")
        cur = sql.cursor()
        cur.execute("SELECT * FROM users WHERE name LIKE ?;", ["%"+user+"%"])
        search_users = cur.fetchall()
        sql.commit()
        sql.close()
        return render_template('/search.html', users=search_users)
    return render_template('/search.html')

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        points = request.form['points']
        sql = sqlite3.connect("database.db")
        cur = sql.cursor()
        cur.execute("INSERT INTO users (name, id, points) VALUES (?, ?, ?);", (name, id, points))
        sql.commit()
        sql.close()
        return redirect('http://127.0.0.1:5000')
    return render_template('/create.html')

@app.route('/delete/<id>', methods=('POST',))
def delete(id):
    sql = sqlite3.connect("database.db")
    cur = sql.cursor()
    cur.execute("DELETE FROM users WHERE id=?;", (id,))
    sql.commit()
    sql.close()
    return redirect('http://127.0.0.1:5000')
