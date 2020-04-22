import pymysql
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

from Login.settings import (
    MYSQL_DATABASE_USER,
    MYSQL_DATABASE_PASSWORD,
    MYSQL_DATABASE_DB,
    MYSQL_DATABASE_HOST,
)

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/submit", methods=["POST"])
def add_user():
    _json = request.json
    try:
        program = _json["program"]
        name = _json["name"]
        data = _json["data"]
        if not program or not name or not data:
            return "Empty program/name/data"
        return "Request acknowledged"

    except Exception as e:
        print(e)
    finally:
        return "Request invalid! Must include program, name, data"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
