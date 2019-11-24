delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_size;

CREATE FUNCTION resource_statistic_standard_deviation_size() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV FLOAT;
    select STD(ResponseSize) into STD_DEV from PING;
    RETURN STD_DEV;
END//

delimiter ;