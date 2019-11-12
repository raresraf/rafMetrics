import pymysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

from flaskext.mysql import MySQL
import os


from flask import Flask

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'WebMonitoring'
app.config['MYSQL_DATABASE_HOST'] = '10.96.0.2'
mysql.init_app(app)


@app.route('/')
def index():
    return "Hello, world!"

@app.route('/add', methods=['POST'])
def add_user():
    try:
        _json = request.json
        _last_name = _json['last_name']
        _first_name = _json['first_name']
        _username = _json['username']
        _email = _json['email']
        _password = _json['pwd']
        # validate the received values
        if _last_name and _first_name and _username and _email and _password and request.method == 'POST':
            #do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO USERS(LastName, FirstName, Username, Email, hashedpassword) VALUES(%s, %s, %s, %s, %s)"
            data = (_last_name, _first_name, _username , _email, _hashed_password)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/users')
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
        cursor.close()
        conn.close()

@app.route('/user/<id>')
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
        cursor.close()
        conn.close()

@app.route('/update/<id>', methods=['POST'])
def update_user(id):
    try:
        _json = request.json
        _last_name = _json['last_name']
        _first_name = _json['first_name']
        _email = _json['email']
        _password = _json['pwd']
        # validate the received values
        if _last_name and _first_name  and _email and _password and request.method == 'POST':
            #do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "UPDATE USERS SET LastName=%s, FirstName=%s, Email=%s, hashedpassword=%s WHERE Username=%s"
            data = (_last_name ,_first_name, _email, _password, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<id>')
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM USERS WHERE Username=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def get_userid(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM USERS WHERE Username=%s", id)
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/addresource', methods=['POST'])
def add_resource():
    try:
        _json = request.json
        _username = _json['username']
        _resource = _json['resource']
        _command = _json['command']
        # validate the received values
        if _username and _resource and _command and request.method == 'POST':
            # save edits
            get_user_info = get_userid(_username)
            if not get_user_info:
                return not_found()
            _userid = get_user_info.get('Userid', 1)
            sql = "INSERT INTO RESOURCE(Userid, ResourceName, Command) VALUES(%s, %s, %s)"
            data = (_userid, _resource, _command)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Resource added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/addwebsite', methods=['POST'])
def add_website():
    try:
        _json = request.json
        _username = _json['username']
        _website_name = _json['website_name']
        _url = _json['url']
        # validate the received values
        if _username and _website_name and _url and request.method == 'POST':
            # save edits
            get_user_info = get_userid(_username)
            if not get_user_info:
                return not_found()
            _userid = get_user_info.get('Userid', 1)
            sql = "INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl) VALUES(%s, %s, %s)"
            data = (_userid, _website_name, _url)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Website added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

