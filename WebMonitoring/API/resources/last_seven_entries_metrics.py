import pymysql


def get_last_seven_entries_time(mysql, resource_name):
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
        try:
            cursor.close()
            conn.close()
        except NameError:
            return None


def get_last_seven_entries_size(mysql, resource_name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ResponseSize from PING where Resourceid = %s order by Timestamp desc limit 7;"
            % (resource_name))
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
    finally:
        try:
            cursor.close()
            conn.close()
        except NameError:
            return None
