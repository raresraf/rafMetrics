import pymysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

from flaskext.mysql import MySQL
import os

from flask import Flask
from flask_cors import CORS
import math

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


# Less than implementation with None < Anything
def lt_w_none(val1, val2):
    if val1 == None:
        return True
    if val2 == None:
        return True
    return val1 > val2


def get_percent_w_none(val1, val2):
    if val1 == None:
        return 100
    if val2 == None:
        return 0
    return round(abs(val2 - val1) / val1, 2)


def get_last7(resource_name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ResponseTime from PING where Resourceid = %s order by Timestamp desc limit 7;"
            % (resource_name))
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def render_dict(result_args_get, result_args_old_get, list_sample,
                product_name, color):
    return {
        "product": product_name,
        "total": {
            "monthly": round(result_args_get[3], 2),
            "weekly": round(result_args_get[2], 2),
            "daily": round(result_args_get[1], 2),
            "percent": {
                "value":
                get_percent_w_none(result_args_old_get[2], result_args_get[2]),
                "profit":
                lt_w_none(result_args_old_get[2], result_args_get[2])
            }
        },
        "color": color,
        "lowest": {
            "monthly": {
                "value": round(result_args_get[6], 2),
                "profit": lt_w_none(result_args_old_get[6], result_args_get[6])
            },
            "weekly": {
                "value": round(result_args_get[5], 2),
                "profit": lt_w_none(result_args_old_get[5], result_args_get[5])
            },
            "daily": {
                "value": round(result_args_get[4], 2),
                "profit": lt_w_none(result_args_old_get[4], result_args_get[4])
            }
        },
        "median": {
            "monthly": {
                "value": round(result_args_get[9], 2),
                "profit": lt_w_none(result_args_old_get[9], result_args_get[9])
            },
            "weekly": {
                "value": round(result_args_get[8], 2),
                "profit": lt_w_none(result_args_old_get[8], result_args_get[8])
            },
            "daily": {
                "value": round(result_args_get[7], 2),
                "profit": lt_w_none(result_args_old_get[7], result_args_get[7])
            }
        },
        "highest": {
            "monthly": {
                "value": round(result_args_get[12], 2),
                "profit": lt_w_none(result_args_old_get[12],
                                    result_args_get[12])
            },
            "weekly": {
                "value": round(result_args_get[11], 2),
                "profit": lt_w_none(result_args_old_get[11],
                                    result_args_get[11])
            },
            "daily": {
                "value": round(result_args_get[10], 2),
                "profit": lt_w_none(result_args_old_get[10],
                                    result_args_get[10])
            }
        },
        "samples": list_sample
    }


@app.route('/request_time/<resource_name>')
def request_time(resource_name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        """
        Compatibility warning: PEP-249 specifies that any modified
        parameters must be returned. This is currently impossible
        as they are only available by storing them in a server
        variable and then retrieved by a query. Since stored
        procedures return zero or more result sets, there is no
        reliable way to get at OUT or INOUT parameters via callproc.
        The server variables are named @_procname_n, where procname
        is the parameter above and n is the position of the parameter
        (from zero). Once all result sets generated by the procedure
        have been fetched, you can issue a SELECT @_procname_0, ...
        query using .execute() to get any OUT or INOUT values.
        """
        args = [resource_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        cursor.callproc('resource_get_time', args)
        cursor.execute("SELECT @_resource_get_time_0, "
                       "@_resource_get_time_1, "
                       "@_resource_get_time_2, "
                       "@_resource_get_time_3, "
                       "@_resource_get_time_4, "
                       "@_resource_get_time_5, "
                       "@_resource_get_time_6, "
                       "@_resource_get_time_7, "
                       "@_resource_get_time_8, "
                       "@_resource_get_time_9, "
                       "@_resource_get_time_10, "
                       "@_resource_get_time_11, "
                       "@_resource_get_time_12 ")
        result_args_get_time = cursor.fetchone()

        cursor.callproc('resource_get_old_time', args)
        cursor.execute("SELECT @_resource_get_old_time_0, "
                       "@_resource_get_old_time_1, "
                       "@_resource_get_old_time_2, "
                       "@_resource_get_old_time_3, "
                       "@_resource_get_old_time_4, "
                       "@_resource_get_old_time_5, "
                       "@_resource_get_old_time_6, "
                       "@_resource_get_old_time_7, "
                       "@_resource_get_old_time_8, "
                       "@_resource_get_old_time_9, "
                       "@_resource_get_old_time_10, "
                       "@_resource_get_old_time_11, "
                       "@_resource_get_old_time_12 ")
        result_args_old_get_time = cursor.fetchone()

        list_sample = []
        samples = get_last7(resource_name)
        for sample in samples:
            list_sample.append(int(1000 * sample['ResponseTime'] + 1))

        resp = jsonify([
            render_dict(result_args_get_time, result_args_old_get_time,
                        list_sample, "Request Time", "primary"),
            render_dict(result_args_get_time, result_args_old_get_time,
                        list_sample, "Response size", "warning"),
            render_dict(result_args_get_time, result_args_old_get_time,
                        list_sample, "Efficiency", "secondary")
        ])
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
