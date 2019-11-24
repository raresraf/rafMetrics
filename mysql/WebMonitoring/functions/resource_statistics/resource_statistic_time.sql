delimiter //

DROP FUNCTION IF EXISTS resource_statistic_requests;

CREATE FUNCTION resource_statistic_requests() RETURNS INT
BEGIN
    DECLARE TIME_ALL INT;
    select SUM(ResponseTime) into TIME_ALL from PING;
    RETURN TIME_ALL;
END//

delimiter ;