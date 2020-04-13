from flask import jsonify

from Login.app import get_user_id
from Login.app import not_found


def delete_resource_wrapper(mysql, request):
    try:
        _json = request.json
        _username = _json["username"]
        _resource = _json["resource"]
        _command = _json["command"]
        # validate the received values
        if _username and _resource and _command and request.method == "POST":
            # save edits
            get_user_info = get_user_id(_username)
            if not get_user_info:
                return not_found()
            _userid = get_user_info.get("Userid", 1)
            sql = "DELETE FROM RESOURCE where Userid = %s and ResourceName = %s and Command = %s"
            data = (_userid, _resource, _command)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("Resource deleted successfully!")
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
