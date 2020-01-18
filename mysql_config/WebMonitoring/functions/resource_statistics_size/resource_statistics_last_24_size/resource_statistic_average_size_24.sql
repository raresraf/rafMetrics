delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_size_24;

CREATE FUNCTION resource_statistic_average_size_24() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_SIZE_24 FLOAT;
    select AVG(ResponseSize) into AVERAGE_TIME_SIZE_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN AVERAGE_TIME_SIZE_24;
END//

delimiter ;