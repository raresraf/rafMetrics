delimiter //

DROP FUNCTION IF EXISTS resource_statistic_size;

CREATE FUNCTION resource_statistic_size() RETURNS FLOAT
BEGIN
    DECLARE SIZE_ALL FLOAT;
    select SUM(ResponseSize) into SIZE_ALL from PING;
    RETURN SIZE_ALL;
END//

delimiter ;