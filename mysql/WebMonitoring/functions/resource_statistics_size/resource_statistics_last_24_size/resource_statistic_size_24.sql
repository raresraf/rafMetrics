delimiter //

DROP FUNCTION IF EXISTS resource_statistic_size_24;

CREATE FUNCTION resource_statistic_size_24() RETURNS FLOAT
BEGIN
    DECLARE SIZE_24 FLOAT;
    select SUM(ResponseSize) into SIZE_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN SIZE_24;
END//

delimiter ;