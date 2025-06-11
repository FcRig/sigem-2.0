from flask import Blueprint, request, abort, jsonify

users = {}

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True) or request.form
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        abort(400, description="username and password required")
    if username in users:
        abort(400, description="User already exists")
    users[username] = password
    return jsonify(message="registered")


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or request.form
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        abort(400, description="username and password required")
    if users.get(username) != password:
        abort(401, description="Invalid credentials")
    return jsonify(token=username)
