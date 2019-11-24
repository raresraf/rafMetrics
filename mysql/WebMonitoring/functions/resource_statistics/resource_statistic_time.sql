delimiter //

DROP FUNCTION IF EXISTS resource_statistic_time;

CREATE FUNCTION resource_statistic_time() RETURNS FLOAT
BEGIN
    DECLARE TIME_ALL FLOAT;
    select SUM(ResponseTime) into TIME_ALL from PING;
    RETURN TIME_ALL;
END//

delimiter ;