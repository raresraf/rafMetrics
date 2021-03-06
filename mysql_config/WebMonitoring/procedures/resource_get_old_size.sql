-- Size


delimiter //

DROP PROCEDURE IF EXISTS resource_get_size;

CREATE PROCEDURE resource_get_size
(IN id INT,
 OUT average_size_daily FLOAT,
 OUT average_size_weekly FLOAT,
 OUT average_size_monthly FLOAT,
 OUT lowest_size_daily FLOAT,
 OUT lowest_size_weekly FLOAT,
 OUT lowest_size_monthly FLOAT,
 OUT median_size_daily FLOAT,
 OUT median_size_weekly FLOAT,
 OUT median_size_monthly FLOAT,
 OUT highest_size_daily FLOAT,
 OUT highest_size_weekly FLOAT,
 OUT highest_size_monthly FLOAT)

BEGIN

    select avg(ResponseSize) into average_size_daily from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 DAY);
    select avg(ResponseSize) into average_size_weekly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK);
    select avg(ResponseSize) into average_size_monthly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH);
    select min(ResponseSize) into lowest_size_daily from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 DAY);
    select min(ResponseSize) into lowest_size_weekly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK);
    select min(ResponseSize) into lowest_size_monthly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH);
    select x.ResponseSize into median_size_daily from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp > DATE_SUB(now(), INTERVAL 1 DAY) and y.Timestamp > DATE_SUB(now(), INTERVAL 1 DAY) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select x.ResponseSize into median_size_weekly from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK) and y.Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select x.ResponseSize into median_size_monthly from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH) and y.Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH ) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select max(ResponseSize) into highest_size_daily from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 DAY);
    select max(ResponseSize) into highest_size_weekly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 WEEK);
    select max(ResponseSize) into highest_size_monthly from PING where Resourceid = id and Timestamp > DATE_SUB(now(), INTERVAL 1 MONTH);

END//

delimiter ;


delimiter //

DROP PROCEDURE IF EXISTS resource_get_old_size;

CREATE PROCEDURE resource_get_old_size
(IN id INT,
 OUT average_size_daily FLOAT,
 OUT average_size_weekly FLOAT,
 OUT average_size_monthly FLOAT,
 OUT lowest_size_daily FLOAT,
 OUT lowest_size_weekly FLOAT,
 OUT lowest_size_monthly FLOAT,
 OUT median_size_daily FLOAT,
 OUT median_size_weekly FLOAT,
 OUT median_size_monthly FLOAT,
 OUT highest_size_daily FLOAT,
 OUT highest_size_weekly FLOAT,
 OUT highest_size_monthly FLOAT)

BEGIN

    select avg(ResponseSize) into average_size_daily from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and Timestamp > DATE_SUB(now(), INTERVAL 2 DAY);
    select avg(ResponseSize) into average_size_weekly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK);
    select avg(ResponseSize) into average_size_monthly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH) and Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH );
    select min(ResponseSize) into lowest_size_daily from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and Timestamp > DATE_SUB(now(), INTERVAL 2 DAY);
    select min(ResponseSize) into lowest_size_weekly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK);
    select min(ResponseSize) into lowest_size_monthly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH) and Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH);
    select x.ResponseSize into median_size_daily from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and x.Timestamp > DATE_SUB(now(), INTERVAL 2 DAY) and y.Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and y.Timestamp > DATE_SUB(now(), INTERVAL 2 DAY) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select x.ResponseSize into median_size_weekly from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and x.Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK) and y.Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and y.Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select x.ResponseSize into median_size_monthly from PING x, PING y where x.Resourceid = id and y.Resourceid = id and x.Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH ) and x.Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH ) and y.Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH ) and y.Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH ) GROUP BY x.ResponseTime HAVING SUM(SIGN(1-SIGN(y.ResponseTime-x.ResponseTime)))/COUNT(*) > .5 limit 1;
    select max(ResponseSize) into highest_size_daily from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 DAY) and Timestamp > DATE_SUB(now(), INTERVAL 2 DAY);
    select max(ResponseSize) into highest_size_weekly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 WEEK) and Timestamp > DATE_SUB(now(), INTERVAL 2 WEEK);
    select max(ResponseSize) into highest_size_monthly from PING where Resourceid = id and Timestamp < DATE_SUB(now(), INTERVAL 1 MONTH) and Timestamp > DATE_SUB(now(), INTERVAL 2 MONTH);

END//

delimiter ;
