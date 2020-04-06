from mysql_config.generate_init_sql import generate_init_sql
from mysql_config.tests.mock_sql import MOCK_SQL_INIT


def test_init_complete():
    generate_init_sql()
    with open("./mysql_config/init.sql", "r") as init_file:
        init_file_content = init_file.read()
        assert init_file_content == MOCK_SQL_INIT
