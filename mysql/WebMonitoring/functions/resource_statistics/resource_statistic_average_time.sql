delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_time;

CREATE FUNCTION resource_statistic_average_time() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_ALL FLOAT;
    select AVG(ResponseTime) into AVERAGE_TIME_ALL from PING;
    RETURN AVERAGE_TIME_ALL;
END//

delimiter ;