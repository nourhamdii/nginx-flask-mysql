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
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Plateforme de Suivi des Incidents Réseau - Tunisie Telecom</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; }
            .header { background-color: #0056A3; color: white; padding: 25px; border-radius: 8px; }
            .header h1 { margin: 0 0 10px 0; font-size: 26px; }
            .header p { margin: 0; opacity: 0.9; }
            .card { background: white; padding: 20px; margin-top: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .status { color: #28a745; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Plateforme de Suivi des Incidents Réseau - Tunisie Telecom</h1>
            <p>Direction Régionale de Kairouan</p>
        </div>
        <div class="card">
            <h2>Statut de la Plateforme</h2>
            <p><strong>Environnement Cloud :</strong> AWS EC2 / Docker / Terraform / GitHub Actions</p>
            <p><strong>État du service :</strong> <span class="status">Opérationnel 🟢</span></p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)