delimiter //

DROP FUNCTION IF EXISTS resource_get_availability;

CREATE FUNCTION resource_get_availability(RID INT) RETURNS VARCHAR(20)
    BEGIN
        DECLARE COUNT_AVAILABLE INT;
        DECLARE RET_CHAR VARCHAR(20);

        select count(*) total into COUNT_AVAILABLE from PING where Resourceid = RID group by Resourceid;

        IF COUNT_AVAILABLE IS NULL
            THEN
                SET RET_CHAR := 'Unavailable';
            ELSE
                SET RET_CHAR := 'Working';
        END IF;

        RETURN RET_CHAR;
    END//

delimiter ;


select resource_get_availability(12) from dual;
select resource_get_availability(15) from dual;



delimiter //

DROP PROCEDURE IF EXISTS resource_get_time;

CREATE PROCEDURE resource_get_time
    (IN id INT,
     OUT average_time_daily FLOAT,
     OUT average_time_weekly FLOAT,
     OUT average_time_monthly FLOAT,
     OUT lowest_time_daily FLOAT,
     OUT lowest_time_weekly FLOAT,
     OUT lowest_time_monthly FLOAT,
     OUT median_time_daily FLOAT,
     OUT median_time_weekly FLOAT,
     OUT median_time_monthly FLOAT,
     OUT highest_time_daily FLOAT,
     OUT highest_time_weekly FLOAT,
     OUT highest_time_monthly FLOAT)

BEGIN

    select ROUND(avg(ResponseTime), 2) into average_time_daily from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 DAY);
    select ROUND(avg(ResponseTime), 2) into average_time_weekly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK);
    select ROUND(avg(ResponseTime), 2) into average_time_monthly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH);
    select ROUND(min(ResponseTime), 2) into lowest_time_daily from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 DAY);
    select ROUND(min(ResponseTime), 2) into lowest_time_weekly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK);
    select ROUND(min(ResponseTime), 2) into lowest_time_monthly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH);
    select ROUND(x.ResponseTime, 2) into median_time_daily from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp > DATE_SUB(now(), INTERVAL 1 DAY) and y.Timestamp > DATE_SUB(now(), INTERVAL 1 DAY) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select ROUND(x.ResponseTime, 2) into median_time_weekly from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK) and y.Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select ROUND(x.ResponseTime, 2) into median_time_monthly from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH) and y.Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH ) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select ROUND(max(ResponseTime), 2) into highest_time_daily from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 DAY);
    select ROUND(max(ResponseTime), 2) into highest_time_weekly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK);
    select ROUND(max(ResponseTime), 2) into highest_time_monthly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH);

END//

delimiter ;


delimiter //

DROP PROCEDURE IF EXISTS resource_get_old_time;

CREATE PROCEDURE resource_get_old_time
(IN id INT,
 OUT average_time_daily FLOAT,
 OUT average_time_weekly FLOAT,
 OUT average_time_monthly FLOAT,
 OUT lowest_time_daily FLOAT,
 OUT lowest_time_weekly FLOAT,
 OUT lowest_time_monthly FLOAT,
 OUT median_time_daily FLOAT,
 OUT median_time_weekly FLOAT,
 OUT median_time_monthly FLOAT,
 OUT highest_time_daily FLOAT,
 OUT highest_time_weekly FLOAT,
 OUT highest_time_monthly FLOAT)

BEGIN

    select ROUND(avg(ResponseTime), 2) into average_time_daily from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and Timestamp > DATE_SUB(now(), INTERVAL 2 DAY);
    select ROUND(avg(ResponseTime), 2) into average_time_weekly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK);
    select ROUND(avg(ResponseTime), 2) into average_time_monthly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH) and Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH );
    select ROUND(min(ResponseTime), 2) into lowest_time_daily from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and Timestamp > DATE_SUB(now(), INTERVAL 2 DAY);
    select ROUND(min(ResponseTime), 2) into lowest_time_weekly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK);
    select ROUND(min(ResponseTime), 2) into lowest_time_monthly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH) and Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH);
    select ROUND(x.ResponseTime, 2) into median_time_daily from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and x.Timestamp > DATE_SUB(now(), INTERVAL 2 DAY) and y.Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and y.Timestamp > DATE_SUB(now(), INTERVAL 2 DAY) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select ROUND(x.ResponseTime, 2) into median_time_weekly from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and x.Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK) and y.Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and y.Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select ROUND(x.ResponseTime, 2) into median_time_monthly from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH ) and x.Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH ) and y.Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH ) and y.Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH ) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select ROUND(max(ResponseTime), 2) into highest_time_daily from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and Timestamp > DATE_SUB(now(), INTERVAL 2 DAY);
    select ROUND(max(ResponseTime), 2) into highest_time_weekly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK);
    select ROUND(max(ResponseTime), 2) into highest_time_monthly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH) and Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH);

END//

delimiter ;
