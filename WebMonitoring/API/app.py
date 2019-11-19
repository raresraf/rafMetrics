import pymysql
from flask import jsonify
from flask import request

from flaskext.mysql import MySQL

from flask import Flask
from flask_cors import CORS
import math

from metrics_renderer import render_dict
from time_metrics import get_results_resource_get_time
from size_metrics import get_results_resource_get_size

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


@app.route('/resources/metrics/<resource_name>')
def resources_metrics(resource_name):
    (result_args_get_time, result_args_old_get_time,
     list_sample_time) = get_results_resource_get_time(mysql, resource_name)
    (result_args_get_size, result_args_old_get_size,
     list_sample_size) = get_results_resource_get_size(mysql, resource_name)
    resp = jsonify([
        render_dict(result_args_get_time, result_args_old_get_time,
                    list_sample_time, "Request Time", "primary"),
        render_dict(result_args_get_size, result_args_old_get_size,
                    list_sample_size, "Response Size", "warning"),
        render_dict(result_args_get_time, result_args_old_get_time,
                    list_sample_time, "Efficiency", "secondary")
    ])
    resp.status_code = 200
    return resp


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
