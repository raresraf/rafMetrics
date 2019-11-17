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
def available_resources(username):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select r.Resourceid id, r.ResourceName name, r.Command command, r.FirstAdded firstadded, resource_get_availability(r.Resourceid) status from RESOURCE r, USERS u where u.Userid = r.Userid AND u.Username='%s'"
            % (username))
        rows = cursor.fetchall()

        resp = []
        count_id = 0
        for row in rows:
            resp.append(row)
            resp[-1]['id'] = count_id
            count_id = count_id + 1

        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/request_time/<resource_name>')
def request_time(resource_name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute(
            'CALL resource_get_time(1,@a,@b,@c,@d,@e,@f,@g,@h,@i,@j,@k,@l); SELECT @a,@b,@c,@d,@e,@f,@g,@h,@i,@j,@k,@l;'
        )
        rows = cursor.fetchall()

        resp = jsonify(rows)
        """
        resp = jsonify({
            "product": "Response size",
            "total": {
                "monthly": result_args[3],
                "weekly": result_args[2],
                "daily": result_args[1],
                "percent": {
                    "value": 2.5,
                    "profit": True
                }
            },
            "color": "warning",
            "lowest": {
                "monthly": {
                    "value": result_args[6],
                    "profit": True
                },
                "weekly": {
                    "value": result_args[5],
                    "profit": True
                },
                "daily": {
                    "value": result_args[4],
                    "profit": False
                }
            },
            "median": {
                "monthly": {
                    "value": result_args[9],
                    "profit": True
                },
                "weekly": {
                    "value": result_args[8],
                    "profit": False
                },
                "daily": {
                    "value": result_args[7],
                    "profit": False
                }
            },
            "highest": {
                "monthly": {
                    "value": result_args[12],
                    "profit": False
                },
                "weekly": {
                    "value": result_args[11],
                    "profit": True
                },
                "daily": {
                    "value": result_args[10],
                    "profit": True
                }
            },
            "sample": [1, 2, 3, 4, 5, 6, 7]
        })
        resp.status_code = 200
        return resp
        """
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
