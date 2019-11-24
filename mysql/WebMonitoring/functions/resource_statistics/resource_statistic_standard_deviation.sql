delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation;

CREATE FUNCTION resource_statistic_standard_deviation() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV FLOAT;
    select STD(ResponseTime) into STD_DEV from PING;
    RETURN STD_DEV;
END//

delimiter ;