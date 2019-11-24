delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_size_24;

CREATE FUNCTION resource_statistic_standard_deviation_size_24() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV_24 FLOAT;
    select STD(ResponseSize) into STD_DEV_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN STD_DEV_24;
END//

delimiter ;