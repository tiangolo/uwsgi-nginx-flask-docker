from flask import jsonify

from ...core.database import users
from ...main import app
from ..utils import senseless_print


@app.route("/users/")
def route_users():
    users_data = []
    for user in users:
        user_data = {"name": user.name, "email": user.email}
        users_data.append(user_data)
    senseless_print()
    return jsonify(users_data)
