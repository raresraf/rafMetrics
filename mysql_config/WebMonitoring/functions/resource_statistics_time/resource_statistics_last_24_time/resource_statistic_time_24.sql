delimiter //

DROP FUNCTION IF EXISTS resource_statistic_time_24;

CREATE FUNCTION resource_statistic_time_24() RETURNS FLOAT
BEGIN
    DECLARE TIME_24 FLOAT;
    select SUM(ResponseTime) into TIME_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN TIME_24;
END//

delimiter ;