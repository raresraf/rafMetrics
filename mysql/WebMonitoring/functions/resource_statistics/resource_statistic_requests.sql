delimiter //

DROP FUNCTION IF EXISTS resource_statistic_requests;

CREATE FUNCTION resource_statistic_requests() RETURNS INT
BEGIN
    DECLARE COUNT_REQUESTS INT;
    select count(*) total into COUNT_REQUESTS from PING;
    RETURN COUNT_REQUESTS;
END//

delimiter ;