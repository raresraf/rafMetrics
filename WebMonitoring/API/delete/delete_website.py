from flask import jsonify

from Login.app import get_userid
from WebMonitoring.API.app import not_found


def delete_website_wrapper(mysql, request):
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
            sql = "DELETE FROM WEBSITES where Userid = %s and WebsiteName = %s and WebsiteUrl = %s"
            data = (_userid, _website_name, _url)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Website deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
