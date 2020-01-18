EXPECTED_DAILY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE = """delimiter //
DROP PROCEDURE IF EXISTS get_daily_samples_size_websites;
CREATE PROCEDURE get_daily_samples_size_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry0 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Websiteid = id limit 1);
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry1 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Websiteid = id limit 1);
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry2 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Websiteid = id limit 1);
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry3 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Websiteid = id limit 1);
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry4 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Websiteid = id limit 1);
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry5 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1);
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry6 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Websiteid = id limit 1);
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry7 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Websiteid = id limit 1);
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry8 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Websiteid = id limit 1);
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry9 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Websiteid = id limit 1);
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry10 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Websiteid = id limit 1);
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry11 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1);
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry12 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Websiteid = id limit 1);
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry13 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Websiteid = id limit 1);
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry14 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Websiteid = id limit 1);
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry15 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Websiteid = id limit 1);
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry16 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Websiteid = id limit 1);
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry17 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1);
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry18 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Websiteid = id limit 1);
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry19 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Websiteid = id limit 1);
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry20 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Websiteid = id limit 1);
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry21 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Websiteid = id limit 1);
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry22 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Websiteid = id limit 1);
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry23 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1);
        else SET entry23 := 0;
    end if;
END//
delimiter ;
"""

EXPECTED_WEEKLY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE = """delimiter //
DROP PROCEDURE IF EXISTS get_weekly_samples_size_websites;
CREATE PROCEDURE get_weekly_samples_size_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry0 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Websiteid = id limit 1);
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry1 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Websiteid = id limit 1);
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry2 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Websiteid = id limit 1);
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry3 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Websiteid = id limit 1);
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry4 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Websiteid = id limit 1);
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry5 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Websiteid = id limit 1);
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry6 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Websiteid = id limit 1);
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry7 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Websiteid = id limit 1);
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry8 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Websiteid = id limit 1);
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry9 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Websiteid = id limit 1);
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry10 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Websiteid = id limit 1);
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry11 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Websiteid = id limit 1);
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry12 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Websiteid = id limit 1);
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry13 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Websiteid = id limit 1);
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry14 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Websiteid = id limit 1);
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry15 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Websiteid = id limit 1);
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry16 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Websiteid = id limit 1);
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry17 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Websiteid = id limit 1);
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry18 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Websiteid = id limit 1);
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry19 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Websiteid = id limit 1);
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry20 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Websiteid = id limit 1);
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry21 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Websiteid = id limit 1);
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry22 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Websiteid = id limit 1);
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry23 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Websiteid = id limit 1);
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry24 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1);
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry25 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1);
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry26 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1);
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry27 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1);
        else SET entry27 := 0;
    end if;
END//
delimiter ;
"""
EXPECTED_MONTHLY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE = """delimiter //
DROP PROCEDURE IF EXISTS get_monthly_samples_size_websites;
CREATE PROCEDURE get_monthly_samples_size_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT entry28 FLOAT,
    OUT entry29 FLOAT,
    OUT entry30 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select DAY(now()) INTO start_hour;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry0 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Websiteid = id limit 1);
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry1 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Websiteid = id limit 1);
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry2 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Websiteid = id limit 1);
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry3 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Websiteid = id limit 1);
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry4 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Websiteid = id limit 1);
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry5 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Websiteid = id limit 1);
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry6 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Websiteid = id limit 1);
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry7 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Websiteid = id limit 1);
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry8 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Websiteid = id limit 1);
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry9 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Websiteid = id limit 1);
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry10 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Websiteid = id limit 1);
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry11 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Websiteid = id limit 1);
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry12 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Websiteid = id limit 1);
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry13 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Websiteid = id limit 1);
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry14 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Websiteid = id limit 1);
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry15 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Websiteid = id limit 1);
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry16 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Websiteid = id limit 1);
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry17 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Websiteid = id limit 1);
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry18 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Websiteid = id limit 1);
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry19 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Websiteid = id limit 1);
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry20 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Websiteid = id limit 1);
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry21 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Websiteid = id limit 1);
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry22 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Websiteid = id limit 1);
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry23 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Websiteid = id limit 1);
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry24 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Websiteid = id limit 1);
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry25 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Websiteid = id limit 1);
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry26 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Websiteid = id limit 1);
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry27 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Websiteid = id limit 1);
        else SET entry27 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry28 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Websiteid = id limit 1);
        else SET entry28 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry29 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Websiteid = id limit 1);
        else SET entry29 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry30 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Websiteid = id limit 1);
        else SET entry30 := 0;
    end if;
END//
delimiter ;
"""
