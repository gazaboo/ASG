from flask import Flask, Blueprint, request, jsonify, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

APP_PREFIX = '/test_python'
app = Flask(__name__, static_folder='static', static_url_path=f'{APP_PREFIX}/')

# from flask_cors import CORS
# CORS(app, resources={r"/*": {"origins": "http://jilu3758.odns.fr/test_python/"}})
# CORS(app, resources={r"/*": {"origins": "*"}})

DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
PORT = os.getenv('PORT', 5432)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Création de la base de données
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()

# Serve the Vue app for any unmatched routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/create_user', methods=['POST'])
@app.route(f'{APP_PREFIX}/create_user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users', methods=['GET'])
@app.route(f'{APP_PREFIX}/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(users_list), 200

