import os
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'db'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DATABASE', 'tt_db')
    )

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tunisie Telecom - Gestion Réseau</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; }
            .header { background-color: #0056A3; color: white; padding: 20px; border-radius: 8px; }
            .card { background: white; padding: 20px; margin-top: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .status { color: #28a745; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Tunisie Telecom - Direction Régionale</h1>
            <p>Plateforme de Suivi des Incidents Réseau & Infrastructures Cloud</p>
        </div>
        <div class="card">
            <h2>Statut de la Plateforme</h2>
            <p><strong>Environnement :</strong> AWS EC2 / Docker / Terraform CI/CD</p>
            <p><strong>État du service :</strong> <span class="status">Opérationnel 🟢</span></p>
            <p><strong>Région :</strong> Kairouan / Tunisie Telecom</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
