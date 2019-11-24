delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_time;

CREATE FUNCTION resource_statistic_standard_deviation_time() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV FLOAT;
    select STD(ResponseTime) into STD_DEV from PING;
    RETURN STD_DEV;
END//

delimiter ;