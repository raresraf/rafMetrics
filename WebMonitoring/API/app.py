import pymysql
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flaskext.mysql import MySQL

from WebMonitoring.API.constants import PERIOD
from WebMonitoring.API.resources.efficiency_metrics import get_results_resource_get_efficiency
from WebMonitoring.API.resources.metrics_renderer import render_dict
from WebMonitoring.API.resources.samples_time import (
    resources_get_samples_time_daily, resources_get_samples_time_monthly,
    resources_get_samples_time_weekly)
from WebMonitoring.API.resources.size_metrics import get_results_resource_get_size
from WebMonitoring.API.resources.time_metrics import get_results_resource_get_time
from WebMonitoring.API.settings import (MYSQL_DATABASE_HOST,
                                        MYSQL_DATABASE_USER,
                                        MYSQL_DATABASE_PASSWORD,
                                        MYSQL_DATABASE_DB)

app = Flask(__name__)
CORS(app)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] = MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = MYSQL_DATABASE_DB
app.config['MYSQL_DATABASE_HOST'] = MYSQL_DATABASE_HOST
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
            "select r.Resourceid id ,r.Resourceid id_resource, r.ResourceName name, r.Command command, r.FirstAdded firstadded, resource_get_availability(r.Resourceid) status from RESOURCE r, USERS u where u.Userid = r.Userid AND u.Username='%s'"
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
    (result_args_get_efficiency, result_args_old_get_efficiency,
     list_sample_efficiency) = get_results_resource_get_efficiency(
         result_args_get_time, result_args_old_get_time, list_sample_time,
         result_args_get_size, result_args_old_get_size, list_sample_size)
    resp = jsonify([
        render_dict(result_args_get_time,
                    result_args_old_get_time,
                    list_sample_time,
                    "Request Time",
                    "primary",
                    roundDecimal=2),
        render_dict(result_args_get_size,
                    result_args_old_get_size,
                    list_sample_size,
                    "Response Size",
                    "warning",
                    roundDecimal=0),
        render_dict(result_args_get_efficiency,
                    result_args_old_get_efficiency,
                    list_sample_efficiency,
                    "Efficiency",
                    "secondary",
                    roundDecimal=0)
    ])
    resp.status_code = 200
    return resp


@app.route('/resources/samples/time/<resource_id>/<period>')
def resources_get_samples_time(resource_id, period):
    samples = {}
    if period.lower() == PERIOD.DAILY:
        samples = resources_get_samples_time_daily(mysql, resource_id)
    if period.lower() == PERIOD.WEEKLY:
        samples = resources_get_samples_time_weekly(mysql, resource_id)
    if period.lower() == PERIOD.MONTHLY:
        samples = resources_get_samples_time_monthly(mysql, resource_id)

    resp = jsonify(samples)
    resp.status_code = 200
    return resp


@app.route('/resources/statistics')
def resources_statistics():
    try:
        conn = mysql.connect()
        cursor_all = conn.cursor(pymysql.cursors.DictCursor)
        cursor_all.execute(
            "select resource_statistic_requests() requests_all, "
            "resource_statistic_time() time_all, "
            "resource_statistic_average_time() average_time_all, "
            "resource_statistic_standard_deviation() standard_deviation_all "
            "from DUAL")
        fetch = cursor_all.fetchone()
        (requests_all) = fetch

        cursor_24 = conn.cursor(pymysql.cursors.DictCursor)
        cursor_24.execute(
            "select resource_statistic_requests_24() requests_24, "
            "resource_statistic_time_24() time_24, "
            "resource_statistic_average_time_24() average_time_24, "
            "resource_statistic_standard_deviation_24() standard_deviation_24 "
            "from DUAL")
        fetch = cursor_24.fetchone()
        (requests_24) = fetch

        statistics = {
            'requests_24': requests_24['requests_all'],
            'requests_all': requests_all['requests_all'],
            'time_24': requests_24['time_24'],
            'time_all': requests_all['time_all'],
            'average_time_24': requests_24['average_time_24'],
            'average_time_all': requests_all['average_time_all'],
            'sd_time_24': requests_24['standard_deviation_24'],
            'sd_time_all': requests_all['standard_deviation_all'],
            'size_24': 111567,
            'size_all': 111890,
            'average_size_24': 1111.23,
            'average_size_all': 1111.2345,
            'sd_size_24': 1111,
            'sd_size_all': 1112
        }
        resp = jsonify(statistics)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor_all.close()
        cursor_24.close()
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
