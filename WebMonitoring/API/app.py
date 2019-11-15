import pymysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

from flaskext.mysql import MySQL
import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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


@app.route('/availableResources/<username>')
def index(username):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select r.ResourceName, r.Command, r.FirstAdded, resource_get_availability(Resourceid) from RESOURCE r, USERS u where u.Userid = r.Userid AND Username=%s",
            username)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
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
