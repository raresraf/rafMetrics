-- Time

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