delimiter //

DROP FUNCTION IF EXISTS resource_statistic_requests_24;

CREATE FUNCTION resource_statistic_requests_24() RETURNS INT
BEGIN
    DECLARE COUNT_REQUESTS_24 INT;
    select count(*) total into COUNT_REQUESTS_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN COUNT_REQUESTS_24;
END//

delimiter ;