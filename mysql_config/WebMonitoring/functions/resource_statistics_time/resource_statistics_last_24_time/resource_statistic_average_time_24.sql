delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_time_24;

CREATE FUNCTION resource_statistic_average_time_24() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_ALL_24 FLOAT;
    select AVG(ResponseTime) into AVERAGE_TIME_ALL_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN AVERAGE_TIME_ALL_24;
END//

delimiter ;