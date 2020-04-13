import pymysql
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flaskext.mysql import MySQL

from WebMonitoring.API.add.add_resource import add_resource_wrapper
from WebMonitoring.API.add.add_website import add_website_wrapper
from WebMonitoring.API.constants import PERIOD
from WebMonitoring.API.delete.delete_resource import delete_resource_wrapper
from WebMonitoring.API.delete.delete_website import delete_website_wrapper
from WebMonitoring.API.resources.efficiency_metrics import (
    get_results_resource_get_efficiency, )
from WebMonitoring.API.resources.metrics_renderer import render_dict
from WebMonitoring.API.resources.samples_size_resource import (
    resources_get_samples_size_daily,
    resources_get_samples_size_monthly,
    resources_get_samples_size_weekly,
)
from WebMonitoring.API.resources.samples_time_resource import (
    resources_get_samples_time_daily,
    resources_get_samples_time_monthly,
    resources_get_samples_time_weekly,
)
from WebMonitoring.API.resources.size_metrics import get_results_resource_get_size
from WebMonitoring.API.resources.time_metrics import get_results_resource_get_time
from WebMonitoring.API.settings import (
    MYSQL_DATABASE_HOST,
    MYSQL_DATABASE_USER,
    MYSQL_DATABASE_PASSWORD,
    MYSQL_DATABASE_DB,
)
from WebMonitoring.API.websites.samples_size_websites import (
    websites_get_samples_size_daily,
    websites_get_samples_size_weekly,
    websites_get_samples_size_monthly,
)
from WebMonitoring.API.websites.samples_time_websites import (
    websites_get_samples_time_daily,
    websites_get_samples_time_weekly,
    websites_get_samples_time_monthly,
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


@app.route("/availableResources/<username>")
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
            resp[-1]["id"] = count_id
            count_id = count_id + 1

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


@app.route("/availableWebsites/<username>")
def available_websites(username):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select r.Websiteid id ,r.Websiteid id_resource, r.WebsiteName name, r.WebsiteUrl command, r.FirstAdded firstadded, \"WORKING\" status from WEBSITES r, USERS u where u.Userid = r.Userid AND u.Username='%s'"
            % (username))
        rows = cursor.fetchall()

        resp = []
        count_id = 0
        for row in rows:
            resp.append(row)
            resp[-1]["id"] = count_id
            count_id = count_id + 1

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


@app.route("/resources/metrics/<resource_name>")
def resources_metrics(resource_name):
    (
        result_args_get_time,
        result_args_old_get_time,
        list_sample_time,
    ) = get_results_resource_get_time(mysql, resource_name)
    (
        result_args_get_size,
        result_args_old_get_size,
        list_sample_size,
    ) = get_results_resource_get_size(mysql, resource_name)
    (
        result_args_get_efficiency,
        result_args_old_get_efficiency,
        list_sample_efficiency,
    ) = get_results_resource_get_efficiency(
        result_args_get_time,
        result_args_old_get_time,
        list_sample_time,
        result_args_get_size,
        result_args_old_get_size,
        list_sample_size,
    )
    resp = jsonify([
        render_dict(
            result_args_get_time,
            result_args_old_get_time,
            list_sample_time,
            "Request Time",
            "primary",
            roundDecimal=2,
        ),
        render_dict(
            result_args_get_size,
            result_args_old_get_size,
            list_sample_size,
            "Response Size",
            "warning",
            roundDecimal=0,
        ),
        render_dict(
            result_args_get_efficiency,
            result_args_old_get_efficiency,
            list_sample_efficiency,
            "Efficiency",
            "secondary",
            roundDecimal=0,
        ),
    ])
    resp.status_code = 200
    return resp


@app.route("/resources/samples/time/<resource_id>/<period>")
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


@app.route("/websites/samples/time/<website_id>/<period>")
def websites_get_samples_time(website_id, period):
    samples = {}
    if period.lower() == PERIOD.DAILY:
        samples = websites_get_samples_time_daily(mysql, website_id)
    if period.lower() == PERIOD.WEEKLY:
        samples = websites_get_samples_time_weekly(mysql, website_id)
    if period.lower() == PERIOD.MONTHLY:
        samples = websites_get_samples_time_monthly(mysql, website_id)

    resp = jsonify(samples)
    resp.status_code = 200
    return resp


@app.route("/resources/samples/size/<resource_id>/<period>")
def resources_get_samples_size(resource_id, period):
    samples = {}
    if period.lower() == PERIOD.DAILY:
        samples = resources_get_samples_size_daily(mysql, resource_id)
    if period.lower() == PERIOD.WEEKLY:
        samples = resources_get_samples_size_weekly(mysql, resource_id)
    if period.lower() == PERIOD.MONTHLY:
        samples = resources_get_samples_size_monthly(mysql, resource_id)

    resp = jsonify(samples)
    resp.status_code = 200
    return resp


@app.route("/websites/samples/size/<website_id>/<period>")
def websites_get_samples_size(website_id, period):
    samples = {}
    if period.lower() == PERIOD.DAILY:
        samples = websites_get_samples_size_daily(mysql, website_id)
    if period.lower() == PERIOD.WEEKLY:
        samples = websites_get_samples_size_weekly(mysql, website_id)
    if period.lower() == PERIOD.MONTHLY:
        samples = websites_get_samples_size_monthly(mysql, website_id)

    resp = jsonify(samples)
    resp.status_code = 200
    return resp


@app.route("/resources/statistics")
def resources_statistics():
    try:
        conn = mysql.connect()

        # Time
        cursor_all_time = conn.cursor(pymysql.cursors.DictCursor)
        cursor_all_time.execute(
            "select resource_statistic_requests_time() requests_all, "
            "resource_statistic_time() time_all, "
            "resource_statistic_average_time() average_time_all, "
            "resource_statistic_standard_deviation_time() standard_deviation_all "
            "from DUAL")
        fetch = cursor_all_time.fetchone()
        (requests_all) = fetch

        cursor_24_time = conn.cursor(pymysql.cursors.DictCursor)
        cursor_24_time.execute(
            "select resource_statistic_requests_time_24() requests_24, "
            "resource_statistic_time_24() time_24, "
            "resource_statistic_average_time_24() average_time_24, "
            "resource_statistic_standard_deviation_time_24() standard_deviation_24 "
            "from DUAL")
        fetch = cursor_24_time.fetchone()
        (requests_24) = fetch

        # Size
        cursor_all_size = conn.cursor(pymysql.cursors.DictCursor)
        cursor_all_size.execute(
            "select "
            "resource_statistic_size() size_all, "
            "resource_statistic_average_size() average_size_all, "
            "resource_statistic_standard_deviation_size() standard_deviation_all "
            "from DUAL")
        fetch = cursor_all_size.fetchone()
        (requests_all_size) = fetch

        cursor_24_size = conn.cursor(pymysql.cursors.DictCursor)
        cursor_24_size.execute(
            "select "
            "resource_statistic_size_24() size_24, "
            "resource_statistic_average_size_24() average_size_24, "
            "resource_statistic_standard_deviation_size_24() standard_deviation_24 "
            "from DUAL")
        fetch = cursor_24_size.fetchone()
        (requests_24_size) = fetch

        statistics = {
            "requests_24": round(requests_24["requests_24"], 2),
            "requests_all": round(requests_all["requests_all"], 2),
            "time_24": round(requests_24["time_24"], 2),
            "time_all": round(requests_all["time_all"], 2),
            "average_time_24": round(requests_24["average_time_24"], 2),
            "average_time_all": round(requests_all["average_time_all"], 2),
            "sd_time_24": round(requests_24["standard_deviation_24"], 2),
            "sd_time_all": round(requests_all["standard_deviation_all"], 2),
            "size_24": round(requests_24_size["size_24"], 2),
            "size_all": round(requests_all_size["size_all"], 2),
            "average_size_24": round(requests_24_size["average_size_24"], 2),
            "average_size_all": round(requests_all_size["average_size_all"],
                                      2),
            "sd_size_24": round(requests_24_size["standard_deviation_24"], 2),
            "sd_size_all": round(requests_all_size["standard_deviation_all"],
                                 2),
        }
        resp = jsonify(statistics)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        try:
            cursor_all_time.close()
            cursor_24_time.close()
            cursor_all_size.close()
            cursor_24_size.close()
            conn.close()
        except NameError:
            resp = jsonify("Operation failed")
            resp.status_code = 404
            return resp


@app.route("/websites/statistics")
def websites_statistics():
    try:
        conn = mysql.connect()

        # Time
        cursor_all_time = conn.cursor(pymysql.cursors.DictCursor)
        cursor_all_time.execute(
            "select FLOOR(SUM(TotalTime)) time_all, count(*) requests_all, AVG(TotalTime) average_time_all, STD(TotalTime) standard_deviation_all from WEBSITES_METRICS"
        )
        fetch = cursor_all_time.fetchone()
        (requests_all) = fetch

        cursor_24_time = conn.cursor(pymysql.cursors.DictCursor)
        cursor_24_time.execute(
            "select FLOOR(SUM(TotalTime)) time_24, count(*) requests_24, AVG(TotalTime) average_time_24, STD(TotalTime) standard_deviation_24 from WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR)"
        )
        fetch = cursor_24_time.fetchone()
        (requests_24) = fetch

        # Size
        cursor_all_size = conn.cursor(pymysql.cursors.DictCursor)
        cursor_all_size.execute(
            "select SUM(bodySize) size_all, AVG(bodySize) average_size_all, STD(bodySize) standard_deviation_all from REQUESTS"
        )
        fetch = cursor_all_size.fetchone()
        (requests_all_size) = fetch

        cursor_24_size = conn.cursor(pymysql.cursors.DictCursor)
        cursor_24_size.execute(
            "select SUM(bodySize) size_24, AVG(bodySize) average_size_24, STD(bodySize) standard_deviation_24 from REQUESTS WHERE startedDateTime >= DATE_SUB(NOW(), INTERVAL 24 HOUR)"
        )
        fetch = cursor_24_size.fetchone()
        (requests_24_size) = fetch

        statistics = {
            "requests_24": round(requests_24["requests_24"], 2),
            "requests_all": round(requests_all["requests_all"], 2),
            "time_24": round(requests_24["time_24"], 2),
            "time_all": round(requests_all["time_all"], 2),
            "average_time_24": round(requests_24["average_time_24"], 2),
            "average_time_all": round(requests_all["average_time_all"], 2),
            "sd_time_24": round(requests_24["standard_deviation_24"], 2),
            "sd_time_all": round(requests_all["standard_deviation_all"], 2),
            "size_24": round(requests_24_size["size_24"], 2),
            "size_all": round(requests_all_size["size_all"], 2),
            "average_size_24": round(requests_24_size["average_size_24"], 2),
            "average_size_all": round(requests_all_size["average_size_all"],
                                      2),
            "sd_size_24": round(requests_24_size["standard_deviation_24"], 2),
            "sd_size_all": round(requests_all_size["standard_deviation_all"],
                                 2),
        }
        resp = jsonify(statistics)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        try:
            cursor_all_time.close()
            cursor_24_time.close()
            cursor_all_size.close()
            cursor_24_size.close()
            conn.close()
        except NameError:
            resp = jsonify("Operation failed")
            resp.status_code = 404
            return resp


@app.route("/addresource", methods=["POST"])
def add_resource():
    return add_resource_wrapper(mysql, request)


@app.route("/addwebsite", methods=["POST"])
def add_website():
    return add_website_wrapper(mysql, request)


@app.route("/deleteresource", methods=["POST"])
def delete_resource():
    return delete_resource_wrapper(mysql, request)


@app.route("/deletewebsite", methods=["POST"])
def delete_website():
    return delete_website_wrapper(mysql, request)


@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
