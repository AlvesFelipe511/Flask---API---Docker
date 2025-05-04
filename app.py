from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}/{os.getenv("POSTGRES_DB")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)


with app.app_context():
    db.create_all()


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(force=True)
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário adicionado com sucesso!'})


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{'id': u.id, 'name': u.name, 'email': u.email} for u in users]
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
