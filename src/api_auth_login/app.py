from flask import Flask, request

app = Flask(__name__)

users = []
users_id = 1

@app.route('/')
def index():
    return 'Hello world'

@app.route("/register", methods=['POST'])
def register_user():
    global users_id
    data = request.get_json()
    return ''

if __name__ == "__main__":
    app.run(debug=True)
