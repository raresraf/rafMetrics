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

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = MYSQL_DATABASE_USER
app.config["MYSQL_DATABASE_PASSWORD"] = MYSQL_DATABASE_PASSWORD
app.config["MYSQL_DATABASE_DB"] = MYSQL_DATABASE_DB
app.config["MYSQL_DATABASE_HOST"] = MYSQL_DATABASE_HOST

# Workaround for KeyError: MYSQL_DATABASE_SOCKET
app.config["MYSQL_DATABASE_SOCKET"] = None

mysql.init_app(app)


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/add", methods=["POST"])
def add_user():
    try:
        _json = request.json
        _last_name = _json["last_name"]
        _first_name = _json["first_name"]
        _username = _json["username"]
        _email = _json["email"]
        _password = _json["pwd"]
        # Validate the received values
        if (_last_name and _first_name and _username and _email and _password
                and request.method == "POST"):
            # Get password hash
            _hashed_password = generate_password_hash(_password)
            # Save edits
            sql = "INSERT INTO USERS(LastName, FirstName, Username, Email, hashedpassword) VALUES(%s, %s, %s, %s, %s)"
            data = (_last_name, _first_name, _username, _email,
                    _hashed_password)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("User added successfully!")
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except NameError:
            resp = jsonify("Operation failed")
            resp.status_code = 404
            return resp


@app.route("/users")
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM USERS")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except NameError:
            resp = jsonify("Operation failed")
            resp.status_code = 404
            return resp


@app.route("/user/<id>")
def user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM USERS WHERE Username=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except NameError:
            resp = jsonify("Operation failed")
            resp.status_code = 404
            return resp


def get_user_id(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM USERS WHERE Username=%s", id)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except NameError:
            resp = jsonify("Operation failed")
            resp.status_code = 404
            return resp


@app.route("/user/<id>/<passwd>")
def auth_user(id, passwd):
    try:
        row = get_user_id(id)
        ref_passwd = ""
        if row:
            ref_passwd = row.get("hashedpassword", "")
        if check_password_hash(ref_passwd, passwd):
            resp = jsonify(authenticated=True)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify(authenticated=False)
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)


@app.route("/update/<id>", methods=["POST"])
def update_user(id):
    try:
        _json = request.json
        _last_name = _json["last_name"]
        _first_name = _json["first_name"]
        _email = _json["email"]
        _password = _json["pwd"]
        # Validate the received values
        if (_last_name and _first_name and _email and _password
                and request.method == "POST"):
            # Get password hash
            _hashed_password = generate_password_hash(_password)
            # Save edits
            sql = "UPDATE USERS SET LastName=%s, FirstName=%s, Email=%s, hashedpassword=%s WHERE Username=%s"
            data = (_last_name, _first_name, _email, _hashed_password, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("User updated successfully!")
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except NameError:
            resp = jsonify("Operation failed")
            resp.status_code = 404
            return resp


@app.route("/delete/<id>")
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM USERS WHERE Username=%s", (id, ))
        conn.commit()
        resp = jsonify("User deleted successfully!")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except NameError:
            resp = jsonify("Operation failed")
            resp.status_code = 404
            return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
