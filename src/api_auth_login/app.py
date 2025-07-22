from flask import Flask, jsonify, request
from passlib.context import CryptContext

from utils import is_valid_email

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = Flask(__name__)

users = []
users_id = 1

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

@app.route('/')
def index():
    return 'Hello world'

@app.route("/register", methods=['POST'])
def register_user():
    global users_id
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    hashed_password = hash_password(password)
    if is_valid_email(email):
        if not any(u['email'] == email for u in users):
            new_user = {
                'id': users_id,
                'email': email,
                'password': hashed_password,
            }
            users.append(new_user)
            users_id += 1
            return jsonify({'message': 'Usuário cadastrado com sucesso'}), 201
        return jsonify({'message': 'E-mail já cadastrado'}), 404
    return jsonify({'message': 'Digite um e-mail válido'}), 404

@app.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if is_valid_email(email):
        user = next((u for u in users if u['email'] == email), None)
        if not user or not verify_password(password, user['password']):
            return jsonify({'message': 'Usuário não encontrado'}), 404
        return jsonify({'message': 'Entrou no sistema!'}), 201
    return jsonify({'message': 'Digite um e-mail válido'}), 404

if __name__ == "__main__":
    app.run(debug=True)
