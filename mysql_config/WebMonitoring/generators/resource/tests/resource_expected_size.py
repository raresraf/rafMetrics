EXPECTED_DAILY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE = """delimiter //
DROP PROCEDURE IF EXISTS get_daily_samples_size;
CREATE PROCEDURE get_daily_samples_size (
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
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Resourceid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Resourceid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Resourceid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Resourceid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Resourceid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Resourceid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Resourceid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Resourceid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Resourceid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Resourceid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Resourceid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Resourceid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Resourceid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Resourceid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Resourceid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Resourceid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Resourceid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Resourceid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Resourceid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Resourceid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id limit 1;
        else SET entry23 := 0;
    end if;
END//
delimiter ;
"""
EXPECTED_WEEKLY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE = """delimiter //
DROP PROCEDURE IF EXISTS get_weekly_samples_size;
CREATE PROCEDURE get_weekly_samples_size (
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
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Resourceid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Resourceid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Resourceid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Resourceid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Resourceid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Resourceid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Resourceid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Resourceid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Resourceid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Resourceid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Resourceid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Resourceid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Resourceid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Resourceid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Resourceid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Resourceid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Resourceid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Resourceid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Resourceid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Resourceid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Resourceid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Resourceid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Resourceid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Resourceid = id limit 1;
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry24 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id limit 1;
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry25 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id limit 1;
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry26 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id limit 1;
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id)
        then SELECT ResponseSize INTO entry27 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id limit 1;
        else SET entry27 := 0;
    end if;
END//
delimiter ;
"""

EXPECTED_MONTHLY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE = """delimiter //
DROP PROCEDURE IF EXISTS get_monthly_samples_size;
CREATE PROCEDURE get_monthly_samples_size (
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
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Resourceid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Resourceid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Resourceid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Resourceid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Resourceid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Resourceid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Resourceid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Resourceid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Resourceid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Resourceid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Resourceid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Resourceid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Resourceid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Resourceid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Resourceid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Resourceid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Resourceid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Resourceid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Resourceid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Resourceid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Resourceid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Resourceid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Resourceid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Resourceid = id limit 1;
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry24 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Resourceid = id limit 1;
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry25 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Resourceid = id limit 1;
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry26 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Resourceid = id limit 1;
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry27 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Resourceid = id limit 1;
        else SET entry27 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry28 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Resourceid = id limit 1;
        else SET entry28 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry29 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Resourceid = id limit 1;
        else SET entry29 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Resourceid = id)
        then SELECT ResponseSize INTO entry30 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Resourceid = id limit 1;
        else SET entry30 := 0;
    end if;
END//
delimiter ;
"""
