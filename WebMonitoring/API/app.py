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

