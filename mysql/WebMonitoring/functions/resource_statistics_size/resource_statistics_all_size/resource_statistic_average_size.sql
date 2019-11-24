delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_size;

CREATE FUNCTION resource_statistic_average_size() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_SIZE_ALL FLOAT;
    select AVG(ResponseSize) into AVERAGE_SIZE_ALL from PING;
    RETURN AVERAGE_SIZE_ALL;
END//

delimiter ;