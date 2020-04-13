from mysql_config.settings import SQL_INIT_FILES


def generate_init_sql():
    # Generate SQL init file for dockerized deployment

    f = open("./mysql_config/init.sql", "w")

    f.write("# Auto-generated init SQL file.\n")
    f.write("# Do not manually edit this file.\n\n\n")
    f.write("CREATE DATABASE IF NOT EXISTS WebMonitoring;\n\n")
    f.write("use WebMonitoring;\n\n\n")

    for tmpfile_name in SQL_INIT_FILES:
        with open(tmpfile_name, "r") as tmpfile:
            tmpfile_read = tmpfile.read()
            f.write(tmpfile_read)
            f.write("\n")


if __name__ == "__main__":
    generate_init_sql()
