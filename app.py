from flask_sqlalchemy import SQLAlchemy
import os
import random
import string
from flask import Flask, request, jsonify, url_for
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@127.0.0.1:5432/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def create_random_user():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    email = f"{username}@example.com"
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Random user created successfully', 'username': username, 'email': email}), 201

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201