import mock

from Login.app import index, add_user, app

from mock import MagicMock

from Login.settings import MYSQL_DATABASE_USER, MYSQL_DATABASE_PASSWORD, MYSQL_DATABASE_DB, MYSQL_DATABASE_HOST


def test_index():
    ret_index_msg = index()
    assert ret_index_msg == "Hello, world!"


@mock.patch('Login.app.generate_password_hash')
@mock.patch('Login.app.mysql')
def test_add_user(mocked_mysql_var, mocked_hash):
    with app.test_request_context('/add',
                                  json={
                                      "last_name": "flask_test_last_name",
                                      "first_name": "flask_test_first_name",
                                      "username": "flask_test_username",
                                      "email": "flask_test_email",
                                      "pwd": "flask_test_password"
                                  },
                                  method="POST"):

        # Same Hash Gen
        mocked_hash.return_value = 'pbkdf2:sha256:150000$uQP6jkPa$a70e2bab07128ebf878ba0e0c6ea03a6f397794b36c794bac2087c944d03b40b'

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
            'INSERT INTO USERS(LastName, FirstName, Username, Email, hashedpassword) VALUES(%s, %s, %s, %s, %s)',
            ('flask_test_last_name', 'flask_test_first_name',
             'flask_test_username', 'flask_test_email',
             'pbkdf2:sha256:150000$uQP6jkPa$a70e2bab07128ebf878ba0e0c6ea03a6f397794b36c794bac2087c944d03b40b'
             ))
        conn.commit.assert_called_once_with()
        assert resp.status_code == 200
        assert resp.json == 'User added successfully!'
        cursor.close.assert_called_once_with()
        conn.close.assert_called_once_with()
