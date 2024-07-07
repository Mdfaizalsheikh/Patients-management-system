import sqlite3

def connect():
    conn = sqlite3.connect('patients.db')
    cur = conn.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS patient
           (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, contact TEXT)'''
    )
    conn.commit()
    conn.close()

def insert(name, age, gender, contact):
    conn = sqlite3.connect('patients.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO patient VALUES (NULL, ?, ?, ?, ?)", (name, age, gender, contact))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('patients.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM patient")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('patients.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM patient WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, age, gender, contact):
    conn = sqlite3.connect('patients.db')
    cur = conn.cursor()
    cur.execute("UPDATE patient SET name=?, age=?, gender=?, contact=? WHERE id=?", (name, age, gender, contact, id))
    conn.commit()
    conn.close()

connect()
