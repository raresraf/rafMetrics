import sys


def website_generate_samples_queries_size(period):
    procedure_name = "get_" + period.lower() + "_samples_size_websites"

    howmany = 24
    GOBACK = "HOUR"
    COEF = 1
    if period.lower() == "daily":
        howmany = 24
        GOBACK = "HOUR"
        COEF = 1
    elif period.lower() == "weekly":
        howmany = 7 * 4
        GOBACK = "HOUR"
        COEF = 6
    elif period.lower() == "monthly":
        howmany = 31
        GOBACK = "DAY"
        COEF = 1

    print("delimiter //")
    print("DROP PROCEDURE IF EXISTS %s;" % procedure_name)
    print("CREATE PROCEDURE %s (" % procedure_name)
    print("    IN id INT,")
    for i in range(howmany):
        print("    OUT entry%d FLOAT," % i)
    print("    OUT start_hour FLOAT")
    print(" )")

    print("BEGIN")
    if period.lower() == "monthly":
        print("    select DAY(now()) INTO start_hour;")
    else:
        print("    select HOUR(now()) INTO start_hour;")

    for i in range(howmany):
        print(
            "    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL %d %s) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL %d %s) AND Websiteid = id limit 1))"
            % (COEF * (howmany - i), GOBACK, COEF * (howmany - 1 - i), GOBACK))
        print(
            "        then SELECT SUM(bodySize) INTO entry%d from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL %d %s) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL %d %s) AND Websiteid = id limit 1);"
            % (i, COEF * (howmany - i), GOBACK, COEF *
               (howmany - 1 - i), GOBACK))
        print("        else SET entry%d := 0;" % i)
        print("    end if;")

    print("END//")
    print("delimiter ;")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(
            "Usage: python3 website_generate_samples_queries_size.py <period>")
        sys.exit(-1)
    website_generate_samples_queries_size(sys.argv[1])
