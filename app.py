import requests
import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS 

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# API call
def fetch_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response.json()

# Save data to database
def save_to_db(data):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, body TEXT)')
    cur.executemany('INSERT OR REPLACE INTO posts (id, title, body) VALUES (?, ?, ?)', 
                    [(post['id'], post['title'], post['body']) for post in data])
    conn.commit()
    conn.close()

@app.route('/populate')
def populate():
    data = fetch_data()
    save_to_db(data)
    return 'Data populated successfully'

@app.route('/data')
def get_data():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM posts')
    rows = cur.fetchall()
    conn.close()
    return jsonify([{'id': row[0], 'title': row[1], 'body': row[2]} for row in rows])

if __name__ == '__main__':
    app.run(debug=True)
