import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS todolist (id INTEGER PRIMARY KEY, todo text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM todolist")
        rows = self.cur.fetchall()
        return rows 
    
    def insert(self, todo):
        self.cur.execute("INSERT INTO todolist VALUES (NULL, ?)", (todo,))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM todolist WHERE id=?", (id,))
        self.conn.commit()
        
    def update(self, id, todo):
        self.cur.execute("UPDATE todolist SET todo = ? WHERE id = ?", (todo, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('todos.db')
# db.insert("grocery robinson")
# db.insert("watch netflix")

# python db.py
