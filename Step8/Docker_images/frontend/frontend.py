

from flask import Flask, render_template_string
import requests
import os

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend-service:5001/data")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Dati dal Backend</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f9f9f9; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f0f0f0; }
        .error { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Dati dal Backend</h1>
    {% if error %}
        <p class="error">Errore: {{ error }}</p>
    {% else %}
        <table>
            <thead>
                <tr>
                    {% for key in data[0].keys() %}
                        <th>{{ key }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in data %}
                    <tr>
                        {% for value in row.values() %}
                            <td>{{ value }}</td>
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    try:
        r = requests.get(BACKEND_URL, timeout=5)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, dict):  # converto in lista per gestire il template HTML
            data = [data]
        return render_template_string(HTML_TEMPLATE, data=data, error=None)
    except Exception as e:
        return render_template_string(HTML_TEMPLATE, data=None, error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
