import os

import mock
import pymysql
from mock import MagicMock

from Login.app import (
    index,
    add_user,
    app,
    users,
    user,
    get_user_id,
    auth_user,
    update_user,
    delete_user,
)
from Login.settings import (
    MYSQL_DATABASE_USER,
    MYSQL_DATABASE_DB,
    MYSQL_DATABASE_HOST,
    MYSQL_DATABASE_PASSWORD,
)
from Login.tests.mocks import users_dict


def test_index():
    ret_index_msg = index()
    assert ret_index_msg == "Hello, world!"


@mock.patch("Login.app.generate_password_hash")
@mock.patch("Login.app.mysql")
def test_add_user(mocked_mysql_var, mocked_hash):
    with app.test_request_context(
            "/add",
            json={
                "last_name": "flask_test_last_name",
                "first_name": "flask_test_first_name",
                "username": "flask_test_username",
                "email": "flask_test_email",
                "pwd": "flask_test_password",
            },
            method="POST",
    ):

        # Same Hash Gen
        mocked_hash.return_value = "pbkdf2:sha256:150000$uQP6jkPa$a70e2bab07128ebf878ba0e0c6ea03a6f397794b36c794bac2087c944d03b40b"

        # Establish MySQL connection -- mocked
        conn = MagicMock()
        mocked_mysql_var.connect.return_value = conn

        # Get a MySQL cursor -- mocked
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        cursor.execute.return_value = MagicMock()
        conn.commit.return_value = MagicMock()
        cursor.close.return_value = MagicMock()
        conn.close.return_value = MagicMock()

        # Call add_user procedure
        resp = add_user()

        # Check workflow
        mocked_hash.assert_called_once_with("flask_test_password")
        mocked_mysql_var.connect.assert_called_once_with()
        conn.cursor.assert_called_once_with()
        cursor.execute.assert_called_once_with(
            "INSERT INTO USERS(LastName, FirstName, Username, Email, hashedpassword) VALUES(%s, %s, %s, %s, %s)",
            (
                "flask_test_last_name",
                "flask_test_first_name",
                "flask_test_username",
                "flask_test_email",
                "pbkdf2:sha256:150000$uQP6jkPa$a70e2bab07128ebf878ba0e0c6ea03a6f397794b36c794bac2087c944d03b40b",
            ),
        )
        conn.commit.assert_called_once_with()
        assert resp.status_code == 200
        assert resp.json == "User added successfully!"
        cursor.close.assert_called_once_with()
        conn.close.assert_called_once_with()


@mock.patch("Login.app.mysql")
def test_users(mocked_mysql_var):
    with app.test_request_context("/users"):

        # Establish MySQL connection -- mocked
        conn = MagicMock()
        mocked_mysql_var.connect.return_value = conn

        # Get a MySQL cursor -- mocked
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        cursor.execute.return_value = MagicMock()
        cursor.fetchall.return_value = users_dict
        cursor.close.return_value = MagicMock()
        conn.close.return_value = MagicMock()

        # Call users procedure
        resp = users()
        expected_json = users_dict

        # Check workflow
        mocked_mysql_var.connect.assert_called_once_with()
        conn.cursor.assert_called_once_with(pymysql.cursors.DictCursor)
        cursor.execute.assert_called_once_with("SELECT * FROM USERS")
        assert resp.status_code == 200
        assert resp.json == expected_json
        cursor.close.assert_called_once_with()
        conn.close.assert_called_once_with()


@mock.patch("Login.app.mysql")
def test_user(mocked_mysql_var):
    with app.test_request_context("/user/TestUsername"):

        # Establish MySQL connection -- mocked
        conn = MagicMock()
        mocked_mysql_var.connect.return_value = conn

        # Get a MySQL cursor -- mocked
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        cursor.execute.return_value = MagicMock()
        cursor.fetchone.return_value = users_dict[0]
        cursor.close.return_value = MagicMock()
        conn.close.return_value = MagicMock()

        # Call users procedure
        id = "TestUsername"
        resp = user(id)
        expected_json = users_dict[0]

        # Check workflow
        mocked_mysql_var.connect.assert_called_once_with()
        conn.cursor.assert_called_once_with(pymysql.cursors.DictCursor)
        cursor.execute.assert_called_once_with(
            "SELECT * FROM USERS WHERE Username=%s", id)
        assert resp.status_code == 200
        assert resp.json == expected_json
        cursor.close.assert_called_once_with()
        conn.close.assert_called_once_with()


@mock.patch("Login.app.mysql")
def test_user_id(mocked_mysql_var):

    # Establish MySQL connection -- mocked
    conn = MagicMock()
    mocked_mysql_var.connect.return_value = conn

    # Get a MySQL cursor -- mocked
    cursor = MagicMock()
    conn.cursor.return_value = cursor
    cursor.execute.return_value = MagicMock()
    cursor.fetchone.return_value = users_dict[0]
    cursor.close.return_value = MagicMock()
    conn.close.return_value = MagicMock()

    # Call users procedure
    id = "TestUsername"
    resp = get_user_id(id)
    expected_json = users_dict[0]

    # Check workflow
    mocked_mysql_var.connect.assert_called_once_with()
    conn.cursor.assert_called_once_with(pymysql.cursors.DictCursor)
    cursor.execute.assert_called_once_with(
        "SELECT * FROM USERS WHERE Username=%s", id)
    assert resp == expected_json
    cursor.close.assert_called_once_with()
    conn.close.assert_called_once_with()


@mock.patch("Login.app.mysql")
def test_auth_user_valid_password(mocked_mysql_var):
    with app.test_request_context("/user/<id>/<passwd>"):

        # Establish MySQL connection -- mocked
        conn = MagicMock()
        mocked_mysql_var.connect.return_value = conn

        # Get a MySQL cursor -- mocked
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        cursor.execute.return_value = MagicMock()
        cursor.fetchone.return_value = users_dict[0]
        cursor.close.return_value = MagicMock()
        conn.close.return_value = MagicMock()

        # Call users procedure
        id = "TestUsername"
        passwd = "TestUsername"
        resp = auth_user(id, passwd)
        expected_json = {"authenticated": True}

        # Check workflow
        mocked_mysql_var.connect.assert_called_once_with()
        conn.cursor.assert_called_once_with(pymysql.cursors.DictCursor)
        cursor.execute.assert_called_once_with(
            "SELECT * FROM USERS WHERE Username=%s", id)
        assert resp.status_code == 200
        assert resp.json == expected_json
        cursor.close.assert_called_once_with()
        conn.close.assert_called_once_with()


@mock.patch("Login.app.mysql")
def test_auth_user_invalid_password(mocked_mysql_var):
    with app.test_request_context("/user/<id>/<passwd>"):

        # Establish MySQL connection -- mocked
        conn = MagicMock()
        mocked_mysql_var.connect.return_value = conn

        # Get a MySQL cursor -- mocked
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        cursor.execute.return_value = MagicMock()
        cursor.fetchone.return_value = users_dict[0]
        cursor.close.return_value = MagicMock()
        conn.close.return_value = MagicMock()

        # Call users procedure
        id = "TestUsername"
        passwd = "InvalidPasswd"
        resp = auth_user(id, passwd)
        expected_json = {"authenticated": False}

        # Check workflow
        mocked_mysql_var.connect.assert_called_once_with()
        conn.cursor.assert_called_once_with(pymysql.cursors.DictCursor)
        cursor.execute.assert_called_once_with(
            "SELECT * FROM USERS WHERE Username=%s", id)
        assert resp.status_code == 200
        assert resp.json == expected_json
        cursor.close.assert_called_once_with()
        conn.close.assert_called_once_with()


@mock.patch("Login.app.generate_password_hash")
@mock.patch("Login.app.mysql")
def test_update_user(mocked_mysql_var, mocked_hash):
    with app.test_request_context(
            "/update/TestUsername",
            json={
                "last_name": "flask_test_last_name",
                "first_name": "flask_test_first_name",
                "username": "flask_test_username",
                "email": "flask_test_email",
                "pwd": "flask_test_password",
            },
            method="POST",
    ):

        # Same Hash Gen
        mocked_hash.return_value = "pbkdf2:sha256:150000$uQP6jkPa$a70e2bab07128ebf878ba0e0c6ea03a6f397794b36c794bac2087c944d03b40b"

        # Establish MySQL connection -- mocked
        conn = MagicMock()
        mocked_mysql_var.connect.return_value = conn

        # Get a MySQL cursor -- mocked
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        cursor.execute.return_value = MagicMock()
        conn.commit.return_value = MagicMock()
        cursor.close.return_value = MagicMock()
        conn.close.return_value = MagicMock()

        # Call add_user procedure
        id = "TestUsername"
        resp = update_user(id)

        # Check workflow
        mocked_hash.assert_called_once_with("flask_test_password")
        mocked_mysql_var.connect.assert_called_once_with()
        conn.cursor.assert_called_once_with()
        cursor.execute.assert_called_once_with(
            "UPDATE USERS SET LastName=%s, FirstName=%s, Email=%s, hashedpassword=%s WHERE Username=%s",
            (
                "flask_test_last_name",
                "flask_test_first_name",
                "flask_test_email",
                "pbkdf2:sha256:150000$uQP6jkPa$a70e2bab07128ebf878ba0e0c6ea03a6f397794b36c794bac2087c944d03b40b",
                "TestUsername",
            ),
        )
        conn.commit.assert_called_once_with()
        assert resp.status_code == 200
        assert resp.json == "User updated successfully!"
        cursor.close.assert_called_once_with()
        conn.close.assert_called_once_with()


@mock.patch("Login.app.mysql")
def test_delete(mocked_mysql_var, ):
    with app.test_request_context(
            "/update/TestUsername",
            json={
                "last_name": "flask_test_last_name",
                "first_name": "flask_test_first_name",
                "username": "flask_test_username",
                "email": "flask_test_email",
                "pwd": "flask_test_password",
            },
            method="POST",
    ):

        # Establish MySQL connection -- mocked
        conn = MagicMock()
        mocked_mysql_var.connect.return_value = conn

        # Get a MySQL cursor -- mocked
        cursor = MagicMock()
        conn.cursor.return_value = cursor
        cursor.execute.return_value = MagicMock()
        conn.commit.return_value = MagicMock()
        cursor.close.return_value = MagicMock()
        conn.close.return_value = MagicMock()

        # Call add_user procedure
        id = "TestUsername"
        resp = delete_user(id)

        # Check workflow
        mocked_mysql_var.connect.assert_called_once_with()
        conn.cursor.assert_called_once_with()
        cursor.execute.assert_called_once_with(
            "DELETE FROM USERS WHERE Username=%s", (id, ))
        conn.commit.assert_called_once_with()
        assert resp.status_code == 200
        assert resp.json == "User deleted successfully!"
        cursor.close.assert_called_once_with()
        conn.close.assert_called_once_with()


def test_db_configs():
    assert MYSQL_DATABASE_USER == "root"
    assert MYSQL_DATABASE_PASSWORD == "password"
    assert MYSQL_DATABASE_DB == "WebMonitoring"
    if os.environ.get("DOCKER_COMPOSE_BUILD"):
        assert MYSQL_DATABASE_HOST == "mysql"
    else:
        assert MYSQL_DATABASE_HOST == "10.96.0.2"
