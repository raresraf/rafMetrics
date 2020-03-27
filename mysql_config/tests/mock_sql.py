MOCK_SQL_INIT = """# Auto-generated init SQL file.
# Do not manually edit this file.


CREATE DATABASE IF NOT EXISTS WebMonitoring;

use WebMonitoring;


CREATE table USERS (
    Userid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Username varchar(64) NOT NULL,
    Email varchar(255),
    hashedpassword varchar(2048),
    Created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Userid)
);

CREATE table RESOURCE (
    Resourceid int NOT NULL AUTO_INCREMENT,
    Userid int NOT NULL,
    ResourceName varchar(255) NOT NULL,
    Command varchar(255) NOT NULL,
    FirstAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Resourceid),
    FOREIGN KEY (Userid) REFERENCES USERS(Userid)
);


CREATE table PING (
    Pingid int NOT NULL AUTO_INCREMENT,
    Resourceid int NOT NULL,
    ResponseTime double NOT NULL,
    ResponseSize int NOT NULL,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Pingid),
    FOREIGN KEY (Resourceid) REFERENCES RESOURCE(Resourceid)
);


CREATE table WEBSITES (
    Websiteid int NOT NULL AUTO_INCREMENT,
    Userid int NOT NULL,
    WebsiteName varchar(255) NOT NULL,
    WebsiteUrl varchar(255) UNIQUE,
    FirstAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Websiteid),
    FOREIGN KEY (Userid) REFERENCES USERS(Userid)
);


CREATE table WEBSITES_METRICS (
    Metricid int NOT NULL AUTO_INCREMENT,
    Websiteid int NOT NULL,
    TotalTime double,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Metricid),
    FOREIGN KEY (Websiteid) REFERENCES WEBSITES(Websiteid)
);


CREATE table REQUESTS (
    Requestid int NOT NULL AUTO_INCREMENT,
    Metricid int NOT NULL,
    serverIPAddress varchar(63),
    pageRef varchar(255),
    startedDateTime TIMESTAMP,
    time int,
    responseStatus int,
    headersSize int,
    bodySize int,
    PRIMARY KEY (Requestid),
    FOREIGN KEY (Metricid) REFERENCES WEBSITES_METRICS(Metricid)
);


CREATE table TIMINGS (
    TimingID int NOT NULL AUTO_INCREMENT,
    Requestid int NOT NULL,
    Receive int,
    Send int,
    SSLTime int,
    Connect int,
    DNS int,
    Blocked int,
    Wait int,
    PRIMARY KEY (TimingID),
    FOREIGN KEY (Requestid) REFERENCES REQUESTS(Requestid)
);

CREATE table AUDIT_USERS (
    Userid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Username varchar(64) NOT NULL,
    Email varchar(255),
    hashedpassword varchar(2048),
    action varchar(255),
    Created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Userid)
);
INSERT INTO USERS(LastName, FirstName, Username, Email, hashedpassword)
values ('TestLastName', 'TestFirstName', 'TestUsername', 'TestEmail', 'pbkdf2:sha256:150000$aLUr0Tku$b8bbd76305a65b5fde4c94a22017979c9f3918d251045b0029a07657c9c169fb');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://github.com/raresraf/rafMetrics', 'GET');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://google.com', 'GET');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://www.aliexpress.com/', 'GET');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://www.amazon.com/', 'GET');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://www.emag.ro/', 'GET');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://www.emag.ro/resigilate/tablete/sort-discountdesc/c', 'GET');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://istyle.ro/', 'GET');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://www.piday.org/', 'GET');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'GitHub: rafMetrics', 'https://github.com/raresraf/rafMetrics');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'Google: default webpage', 'https://google.com');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'Aliexpress: default webpage', 'https://www.aliexpress.com/');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'Amazon: default webpage', 'https://www.amazon.com/');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'Emag: default webpage', 'https://www.emag.ro/');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'Emag: tablets sale webpage', 'https://www.emag.ro/resigilate/tablete/sort-discountdesc/c');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'Istyle: default webpage', 'https://istyle.ro/');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'PI Day: 3.14 ', 'https://www.piday.org/');


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
-- Size

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

-- Time

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
delimiter //
DROP PROCEDURE IF EXISTS get_monthly_samples_websites;
CREATE PROCEDURE get_monthly_samples_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT entry28 FLOAT,
    OUT entry29 FLOAT,
    OUT entry30 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select DAY(now()) INTO start_hour;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry0 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Websiteid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry1 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Websiteid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry2 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Websiteid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry3 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Websiteid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry4 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Websiteid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry5 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Websiteid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry6 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Websiteid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry7 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Websiteid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry8 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Websiteid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry9 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Websiteid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry10 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Websiteid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry11 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Websiteid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry12 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Websiteid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry13 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Websiteid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry14 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Websiteid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry15 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Websiteid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry16 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Websiteid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry17 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Websiteid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry18 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Websiteid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry19 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Websiteid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry20 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Websiteid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry21 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Websiteid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry22 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Websiteid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry23 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Websiteid = id limit 1;
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry24 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Websiteid = id limit 1;
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry25 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Websiteid = id limit 1;
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry26 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Websiteid = id limit 1;
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry27 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Websiteid = id limit 1;
        else SET entry27 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry28 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Websiteid = id limit 1;
        else SET entry28 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry29 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Websiteid = id limit 1;
        else SET entry29 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Websiteid = id)
        then SELECT TotalTime INTO entry30 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Websiteid = id limit 1;
        else SET entry30 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_daily_samples_websites;
CREATE PROCEDURE get_daily_samples_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry0 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Websiteid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry1 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Websiteid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry2 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Websiteid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry3 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Websiteid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry4 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Websiteid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry5 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry6 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Websiteid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry7 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Websiteid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry8 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Websiteid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry9 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Websiteid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry10 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Websiteid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry11 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry12 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Websiteid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry13 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Websiteid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry14 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Websiteid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry15 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Websiteid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry16 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Websiteid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry17 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry18 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Websiteid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry19 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Websiteid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry20 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Websiteid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry21 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Websiteid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry22 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Websiteid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry23 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1;
        else SET entry23 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_weekly_samples_websites;
CREATE PROCEDURE get_weekly_samples_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry0 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Websiteid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry1 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Websiteid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry2 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Websiteid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry3 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Websiteid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry4 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Websiteid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry5 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Websiteid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry6 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Websiteid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry7 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Websiteid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry8 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Websiteid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry9 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Websiteid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry10 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Websiteid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry11 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Websiteid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry12 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Websiteid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry13 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Websiteid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry14 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Websiteid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry15 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Websiteid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry16 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Websiteid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry17 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Websiteid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry18 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Websiteid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry19 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Websiteid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry20 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Websiteid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry21 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Websiteid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry22 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Websiteid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry23 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Websiteid = id limit 1;
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry24 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1;
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry25 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1;
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry26 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1;
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT TotalTime FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id)
        then SELECT TotalTime INTO entry27 FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1;
        else SET entry27 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_daily_samples;
CREATE PROCEDURE get_daily_samples (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Resourceid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Resourceid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Resourceid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Resourceid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Resourceid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Resourceid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Resourceid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Resourceid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Resourceid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Resourceid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Resourceid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Resourceid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Resourceid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Resourceid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Resourceid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Resourceid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Resourceid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Resourceid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Resourceid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Resourceid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id limit 1;
        else SET entry23 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_weekly_samples;
CREATE PROCEDURE get_weekly_samples (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Resourceid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Resourceid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Resourceid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Resourceid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Resourceid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Resourceid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Resourceid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Resourceid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Resourceid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Resourceid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Resourceid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Resourceid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Resourceid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Resourceid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Resourceid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Resourceid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Resourceid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Resourceid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Resourceid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Resourceid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Resourceid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Resourceid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Resourceid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Resourceid = id limit 1;
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry24 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id limit 1;
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry25 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id limit 1;
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry26 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id limit 1;
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id)
        then SELECT ResponseTime INTO entry27 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id limit 1;
        else SET entry27 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_monthly_samples;
CREATE PROCEDURE get_monthly_samples (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT entry28 FLOAT,
    OUT entry29 FLOAT,
    OUT entry30 FLOAT,
    OUT start_day FLOAT
 )
BEGIN
    select DAY(now()) INTO start_day;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Resourceid = id limit 1;
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Resourceid = id limit 1;
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Resourceid = id limit 1;
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Resourceid = id limit 1;
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Resourceid = id limit 1;
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Resourceid = id limit 1;
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Resourceid = id limit 1;
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Resourceid = id limit 1;
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Resourceid = id limit 1;
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Resourceid = id limit 1;
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Resourceid = id limit 1;
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Resourceid = id limit 1;
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Resourceid = id limit 1;
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Resourceid = id limit 1;
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Resourceid = id limit 1;
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Resourceid = id limit 1;
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Resourceid = id limit 1;
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Resourceid = id limit 1;
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Resourceid = id limit 1;
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Resourceid = id limit 1;
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Resourceid = id limit 1;
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Resourceid = id limit 1;
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Resourceid = id limit 1;
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Resourceid = id limit 1;
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry24 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Resourceid = id limit 1;
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry25 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Resourceid = id limit 1;
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry26 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Resourceid = id limit 1;
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry27 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Resourceid = id limit 1;
        else SET entry27 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry28 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Resourceid = id limit 1;
        else SET entry28 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry29 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Resourceid = id limit 1;
        else SET entry29 := 0;
    end if;
    if EXISTS(SELECT ResponseTime FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Resourceid = id)
        then SELECT ResponseTime INTO entry30 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Resourceid = id limit 1;
        else SET entry30 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_monthly_samples_size;
CREATE PROCEDURE get_monthly_samples_size (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT entry28 FLOAT,
    OUT entry29 FLOAT,
    OUT entry30 FLOAT,
    OUT start_hour FLOAT
)
BEGIN
    select DAY(now()) INTO start_hour;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Resourceid = id limit 1;
    else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Resourceid = id limit 1;
    else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Resourceid = id limit 1;
    else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Resourceid = id limit 1;
    else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Resourceid = id limit 1;
    else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Resourceid = id limit 1;
    else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Resourceid = id limit 1;
    else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Resourceid = id limit 1;
    else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Resourceid = id limit 1;
    else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Resourceid = id limit 1;
    else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Resourceid = id limit 1;
    else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Resourceid = id limit 1;
    else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Resourceid = id limit 1;
    else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Resourceid = id limit 1;
    else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Resourceid = id limit 1;
    else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Resourceid = id limit 1;
    else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Resourceid = id limit 1;
    else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Resourceid = id limit 1;
    else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Resourceid = id limit 1;
    else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Resourceid = id limit 1;
    else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Resourceid = id limit 1;
    else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Resourceid = id limit 1;
    else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Resourceid = id limit 1;
    else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Resourceid = id limit 1;
    else SET entry23 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry24 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Resourceid = id limit 1;
    else SET entry24 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry25 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Resourceid = id limit 1;
    else SET entry25 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry26 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Resourceid = id limit 1;
    else SET entry26 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry27 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Resourceid = id limit 1;
    else SET entry27 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry28 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Resourceid = id limit 1;
    else SET entry28 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry29 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Resourceid = id limit 1;
    else SET entry29 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Resourceid = id)
    then SELECT ResponseSize INTO entry30 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Resourceid = id limit 1;
    else SET entry30 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_weekly_samples_size;
CREATE PROCEDURE get_weekly_samples_size (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT start_hour FLOAT
)
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Resourceid = id limit 1;
    else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Resourceid = id limit 1;
    else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Resourceid = id limit 1;
    else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Resourceid = id limit 1;
    else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Resourceid = id limit 1;
    else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Resourceid = id limit 1;
    else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Resourceid = id limit 1;
    else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Resourceid = id limit 1;
    else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Resourceid = id limit 1;
    else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Resourceid = id limit 1;
    else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Resourceid = id limit 1;
    else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Resourceid = id limit 1;
    else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Resourceid = id limit 1;
    else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Resourceid = id limit 1;
    else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Resourceid = id limit 1;
    else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Resourceid = id limit 1;
    else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Resourceid = id limit 1;
    else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Resourceid = id limit 1;
    else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Resourceid = id limit 1;
    else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Resourceid = id limit 1;
    else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Resourceid = id limit 1;
    else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Resourceid = id limit 1;
    else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Resourceid = id limit 1;
    else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Resourceid = id limit 1;
    else SET entry23 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry24 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id limit 1;
    else SET entry24 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry25 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id limit 1;
    else SET entry25 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry26 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id limit 1;
    else SET entry26 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry27 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id limit 1;
    else SET entry27 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_daily_samples_size;
CREATE PROCEDURE get_daily_samples_size (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT start_hour FLOAT
)
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry0 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Resourceid = id limit 1;
    else SET entry0 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry1 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Resourceid = id limit 1;
    else SET entry1 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry2 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Resourceid = id limit 1;
    else SET entry2 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry3 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Resourceid = id limit 1;
    else SET entry3 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry4 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Resourceid = id limit 1;
    else SET entry4 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry5 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Resourceid = id limit 1;
    else SET entry5 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry6 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Resourceid = id limit 1;
    else SET entry6 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry7 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Resourceid = id limit 1;
    else SET entry7 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry8 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Resourceid = id limit 1;
    else SET entry8 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry9 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Resourceid = id limit 1;
    else SET entry9 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry10 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Resourceid = id limit 1;
    else SET entry10 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry11 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Resourceid = id limit 1;
    else SET entry11 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry12 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Resourceid = id limit 1;
    else SET entry12 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry13 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Resourceid = id limit 1;
    else SET entry13 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry14 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Resourceid = id limit 1;
    else SET entry14 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry15 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Resourceid = id limit 1;
    else SET entry15 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry16 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Resourceid = id limit 1;
    else SET entry16 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry17 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Resourceid = id limit 1;
    else SET entry17 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry18 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Resourceid = id limit 1;
    else SET entry18 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry19 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Resourceid = id limit 1;
    else SET entry19 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry20 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Resourceid = id limit 1;
    else SET entry20 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry21 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Resourceid = id limit 1;
    else SET entry21 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry22 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Resourceid = id limit 1;
    else SET entry22 := 0;
    end if;
    if EXISTS(SELECT ResponseSize FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id)
    then SELECT ResponseSize INTO entry23 FROM PING WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Resourceid = id limit 1;
    else SET entry23 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_monthly_samples_size_websites;
CREATE PROCEDURE get_monthly_samples_size_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT entry28 FLOAT,
    OUT entry29 FLOAT,
    OUT entry30 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select DAY(now()) INTO start_hour;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry0 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 31 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 DAY) AND Websiteid = id limit 1);
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry1 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 29 DAY) AND Websiteid = id limit 1);
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry2 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 29 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 28 DAY) AND Websiteid = id limit 1);
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry3 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 28 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 27 DAY) AND Websiteid = id limit 1);
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry4 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 27 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 26 DAY) AND Websiteid = id limit 1);
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry5 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 26 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 25 DAY) AND Websiteid = id limit 1);
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry6 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 25 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 DAY) AND Websiteid = id limit 1);
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry7 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 DAY) AND Websiteid = id limit 1);
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry8 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 DAY) AND Websiteid = id limit 1);
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry9 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 DAY) AND Websiteid = id limit 1);
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry10 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 DAY) AND Websiteid = id limit 1);
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry11 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 DAY) AND Websiteid = id limit 1);
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry12 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 DAY) AND Websiteid = id limit 1);
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry13 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 DAY) AND Websiteid = id limit 1);
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry14 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 DAY) AND Websiteid = id limit 1);
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry15 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 DAY) AND Websiteid = id limit 1);
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry16 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 DAY) AND Websiteid = id limit 1);
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry17 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 DAY) AND Websiteid = id limit 1);
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry18 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 DAY) AND Websiteid = id limit 1);
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry19 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 DAY) AND Websiteid = id limit 1);
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry20 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 DAY) AND Websiteid = id limit 1);
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry21 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 DAY) AND Websiteid = id limit 1);
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry22 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 DAY) AND Websiteid = id limit 1);
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry23 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 DAY) AND Websiteid = id limit 1);
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry24 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 DAY) AND Websiteid = id limit 1);
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry25 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 DAY) AND Websiteid = id limit 1);
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry26 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 DAY) AND Websiteid = id limit 1);
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry27 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 DAY) AND Websiteid = id limit 1);
        else SET entry27 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry28 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 DAY) AND Websiteid = id limit 1);
        else SET entry28 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry29 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 DAY) AND Websiteid = id limit 1);
        else SET entry29 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry30 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 DAY) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 DAY) AND Websiteid = id limit 1);
        else SET entry30 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_daily_samples_size_websites;
CREATE PROCEDURE get_daily_samples_size_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry0 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND Websiteid = id limit 1);
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry1 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 23 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND Websiteid = id limit 1);
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry2 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 22 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND Websiteid = id limit 1);
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry3 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 21 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND Websiteid = id limit 1);
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry4 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 20 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND Websiteid = id limit 1);
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry5 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 19 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1);
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry6 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND Websiteid = id limit 1);
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry7 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 17 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND Websiteid = id limit 1);
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry8 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 16 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND Websiteid = id limit 1);
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry9 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 15 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND Websiteid = id limit 1);
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry10 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 14 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND Websiteid = id limit 1);
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry11 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 13 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1);
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry12 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND Websiteid = id limit 1);
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry13 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 11 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND Websiteid = id limit 1);
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry14 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 10 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND Websiteid = id limit 1);
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry15 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 9 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND Websiteid = id limit 1);
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry16 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 8 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND Websiteid = id limit 1);
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry17 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 7 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1);
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry18 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND Websiteid = id limit 1);
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry19 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 5 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND Websiteid = id limit 1);
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry20 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 4 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND Websiteid = id limit 1);
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry21 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 3 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND Websiteid = id limit 1);
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry22 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 2 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND Websiteid = id limit 1);
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry23 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 1 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1);
        else SET entry23 := 0;
    end if;
END//
delimiter ;

delimiter //
DROP PROCEDURE IF EXISTS get_weekly_samples_size_websites;
CREATE PROCEDURE get_weekly_samples_size_websites (
    IN id INT,
    OUT entry0 FLOAT,
    OUT entry1 FLOAT,
    OUT entry2 FLOAT,
    OUT entry3 FLOAT,
    OUT entry4 FLOAT,
    OUT entry5 FLOAT,
    OUT entry6 FLOAT,
    OUT entry7 FLOAT,
    OUT entry8 FLOAT,
    OUT entry9 FLOAT,
    OUT entry10 FLOAT,
    OUT entry11 FLOAT,
    OUT entry12 FLOAT,
    OUT entry13 FLOAT,
    OUT entry14 FLOAT,
    OUT entry15 FLOAT,
    OUT entry16 FLOAT,
    OUT entry17 FLOAT,
    OUT entry18 FLOAT,
    OUT entry19 FLOAT,
    OUT entry20 FLOAT,
    OUT entry21 FLOAT,
    OUT entry22 FLOAT,
    OUT entry23 FLOAT,
    OUT entry24 FLOAT,
    OUT entry25 FLOAT,
    OUT entry26 FLOAT,
    OUT entry27 FLOAT,
    OUT start_hour FLOAT
 )
BEGIN
    select HOUR(now()) INTO start_hour;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry0 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 168 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND Websiteid = id limit 1);
        else SET entry0 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry1 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 162 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND Websiteid = id limit 1);
        else SET entry1 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry2 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 156 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND Websiteid = id limit 1);
        else SET entry2 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry3 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 150 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND Websiteid = id limit 1);
        else SET entry3 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry4 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 144 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND Websiteid = id limit 1);
        else SET entry4 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry5 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 138 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND Websiteid = id limit 1);
        else SET entry5 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry6 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 132 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND Websiteid = id limit 1);
        else SET entry6 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry7 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 126 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND Websiteid = id limit 1);
        else SET entry7 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry8 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 120 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND Websiteid = id limit 1);
        else SET entry8 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry9 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 114 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND Websiteid = id limit 1);
        else SET entry9 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry10 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 108 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND Websiteid = id limit 1);
        else SET entry10 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry11 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 102 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND Websiteid = id limit 1);
        else SET entry11 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry12 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 96 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND Websiteid = id limit 1);
        else SET entry12 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry13 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 90 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND Websiteid = id limit 1);
        else SET entry13 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry14 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 84 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND Websiteid = id limit 1);
        else SET entry14 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry15 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 78 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND Websiteid = id limit 1);
        else SET entry15 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry16 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND Websiteid = id limit 1);
        else SET entry16 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry17 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 66 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND Websiteid = id limit 1);
        else SET entry17 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry18 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 60 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND Websiteid = id limit 1);
        else SET entry18 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry19 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 54 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND Websiteid = id limit 1);
        else SET entry19 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry20 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 48 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND Websiteid = id limit 1);
        else SET entry20 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry21 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 42 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND Websiteid = id limit 1);
        else SET entry21 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry22 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 36 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND Websiteid = id limit 1);
        else SET entry22 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry23 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 30 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND Websiteid = id limit 1);
        else SET entry23 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry24 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND Websiteid = id limit 1);
        else SET entry24 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry25 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 18 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND Websiteid = id limit 1);
        else SET entry25 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry26 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 12 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND Websiteid = id limit 1);
        else SET entry26 := 0;
    end if;
    if EXISTS(SELECT SUM(bodySize) from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1))
        then SELECT SUM(bodySize) INTO entry27 from REQUESTS where Metricid = (SELECT Metricid FROM WEBSITES_METRICS WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 6 HOUR) AND TIMESTAMP <= DATE_SUB(NOW(), INTERVAL 0 HOUR) AND Websiteid = id limit 1);
        else SET entry27 := 0;
    end if;
END//
delimiter ;

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


delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_size_24;

CREATE FUNCTION resource_statistic_average_size_24() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_SIZE_24 FLOAT;
    select AVG(ResponseSize) into AVERAGE_TIME_SIZE_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN AVERAGE_TIME_SIZE_24;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_size_24;

CREATE FUNCTION resource_statistic_standard_deviation_size_24() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV_24 FLOAT;
    select STD(ResponseSize) into STD_DEV_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN STD_DEV_24;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_size_24;

CREATE FUNCTION resource_statistic_size_24() RETURNS FLOAT
BEGIN
    DECLARE SIZE_24 FLOAT;
    select SUM(ResponseSize) into SIZE_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN SIZE_24;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_size;

CREATE FUNCTION resource_statistic_size() RETURNS FLOAT
BEGIN
    DECLARE SIZE_ALL FLOAT;
    select SUM(ResponseSize) into SIZE_ALL from PING;
    RETURN SIZE_ALL;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_size;

CREATE FUNCTION resource_statistic_standard_deviation_size() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV FLOAT;
    select STD(ResponseSize) into STD_DEV from PING;
    RETURN STD_DEV;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_size;

CREATE FUNCTION resource_statistic_average_size() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_SIZE_ALL FLOAT;
    select AVG(ResponseSize) into AVERAGE_SIZE_ALL from PING;
    RETURN AVERAGE_SIZE_ALL;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_requests_time_24;

CREATE FUNCTION resource_statistic_requests_time_24() RETURNS INT
BEGIN
    DECLARE COUNT_REQUESTS_24 INT;
    select count(*) total into COUNT_REQUESTS_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN COUNT_REQUESTS_24;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_time_24;

CREATE FUNCTION resource_statistic_average_time_24() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_ALL_24 FLOAT;
    select AVG(ResponseTime) into AVERAGE_TIME_ALL_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN AVERAGE_TIME_ALL_24;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_time_24;

CREATE FUNCTION resource_statistic_standard_deviation_time_24() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV_24 FLOAT;
    select STD(ResponseTime) into STD_DEV_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN STD_DEV_24;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_time_24;

CREATE FUNCTION resource_statistic_time_24() RETURNS FLOAT
BEGIN
    DECLARE TIME_24 FLOAT;
    select SUM(ResponseTime) into TIME_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN TIME_24;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_time;

CREATE FUNCTION resource_statistic_time() RETURNS FLOAT
BEGIN
    DECLARE TIME_ALL FLOAT;
    select SUM(ResponseTime) into TIME_ALL from PING;
    RETURN TIME_ALL;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_time;

CREATE FUNCTION resource_statistic_standard_deviation_time() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV FLOAT;
    select STD(ResponseTime) into STD_DEV from PING;
    RETURN STD_DEV;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_requests_time;

CREATE FUNCTION resource_statistic_requests_time() RETURNS INT
BEGIN
    DECLARE COUNT_REQUESTS INT;
    select count(*) total into COUNT_REQUESTS from PING;
    RETURN COUNT_REQUESTS;
END//

delimiter ;
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_time;

CREATE FUNCTION resource_statistic_average_time() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_ALL FLOAT;
    select AVG(ResponseTime) into AVERAGE_TIME_ALL from PING;
    RETURN AVERAGE_TIME_ALL;
END//

delimiter ;
CREATE TRIGGER before_users_update
    BEFORE UPDATE ON USERS
    FOR EACH ROW
    INSERT INTO AUDIT_USERS
    SET action = 'update',
        LastName = OLD.LastName,
        FirstName = OLD.FirstName,
        Username = OLD.Username,
        Email = OLD.Email,
        hashedpassword = OLD.hashedpassword;

CREATE TRIGGER before_users_delete
    BEFORE DELETE ON USERS
    FOR EACH ROW
    INSERT INTO AUDIT_USERS
    SET action = 'delete',
        LastName = OLD.LastName,
        FirstName = OLD.FirstName,
        Username = OLD.Username,
        Email = OLD.Email,
        hashedpassword = OLD.hashedpassword;
"""
