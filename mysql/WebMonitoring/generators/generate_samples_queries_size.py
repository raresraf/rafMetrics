import sys


def generate_samples_queries_size(period):
    procedure_name = "get_" + period.lower() + "_samples_size"

    howmany = 24
    GOBACK = 'HOUR'
    COEF = 1
    if period.lower() == 'daily':
        howmany = 24
        GOBACK = 'HOUR'
        COEF = 1
    elif period.lower() == 'weekly':
        howmany = 7 * 4
        GOBACK = 'HOUR'
        COEF = 6
    elif period.lower() == 'monthly':
        howmany = 31
        GOBACK = 'DAY'
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
    print("    select HOUR(now()) INTO start_hour;")

    for i in range(howmany):
        print(
            "    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL %d %s) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL %d %s) AND Resourceid = id)"
            % (COEF * (howmany - i), GOBACK, COEF * (howmany - 1 - i), GOBACK))
        print(
            "        then SELECT ResponseSize INTO entry%d FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL %d %s) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL %d %s) AND Resourceid = id limit 1;"
            % (i, COEF * (howmany - i), GOBACK, COEF *
               (howmany - 1 - i), GOBACK))
        print("        else SET entry%d := 0;" % i)
        print("    end if;")

    print("END//")
    print("delimiter ;")


generate_samples_queries_size(sys.argv[1])