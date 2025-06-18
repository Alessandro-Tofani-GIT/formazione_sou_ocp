from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.getenv('DATABASE_URL')

@app.route('/data')
def get_items():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT * FROM items;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        items = []
        for row in rows:
            items.append({
                "id": row[0],
                "name": row[1],
                "quantity": row[2]
            })
        return jsonify({"items": items})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
