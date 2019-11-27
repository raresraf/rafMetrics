# DB setup
The following steps have to be followed in order to successfully setup the DB:


## MySQL docker image
[mysql:5.6](https://hub.docker.com/_/mysql)
## MySQL deployment in Kubernetes
[Deployment config file](../kubernetes_config/database/mysql-deployment.yaml)

## MySQL init
### Create tables
#### For Platform:

##### USERS
Stores data for all active users registered in the platform
```sql
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

```
#### For Login & Audit:
##### AUDIT_USERS
Audit table used by `before_user_delete` and `before_user_update` triggers.

```sql
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
```


#### For WebMonitoring:
##### RESOURCE
Stores all users' resources to be managed.
```sql
CREATE table RESOURCE (
    Resourceid int NOT NULL AUTO_INCREMENT,
    Userid int NOT NULL,
    ResourceName varchar(255) NOT NULL,
    Command varchar(255) NOT NULL,
    FirstAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Resourceid),
    FOREIGN KEY (Userid) REFERENCES USERS(Userid)
);
```

##### PING
Stores all monitoring results for all resources.

```sql
CREATE table PING (
    Pingid int NOT NULL AUTO_INCREMENT,
    Resourceid int NOT NULL,
    ResponseTime double NOT NULL,
    ResponseSize int NOT NULL,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Pingid),
    FOREIGN KEY (Resourceid) REFERENCES RESOURCE(Resourceid)
);
```

##### WEBSITES
Stores all users' websites to be managed.

```sql
CREATE table WEBSITES (
    Websiteid int NOT NULL AUTO_INCREMENT,
    Userid int NOT NULL,
    WebsiteName varchar(255) NOT NULL,
    WebsiteUrl varchar(255) UNIQUE,
    FirstAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Websiteid),
    FOREIGN KEY (Userid) REFERENCES USERS(Userid)
);
```
##### WEBSITES_METRICS
Stores all monitoring results for all websites.

```sql
CREATE table WEBSITES_METRICS (
    Metricid int NOT NULL AUTO_INCREMENT,
    Websiteid int NOT NULL,
    TotalTime double,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Metricid),
    FOREIGN KEY (Websiteid) REFERENCES WEBSITES(Websiteid)
);
```

##### REQUESTS
Stores all data regarding all requests for all websites.


```sql
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
```

##### TIMINGS
Stores all data regarding all timings for all requests.

```sql
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
```

### Populate tables
Sample simulation to manually populate the DB.
```sql
INSERT INTO USERS(LastName, FirstName, Username, Email, hashedpassword)
values ('TestLastName', 'TestFirstName', 'TestUsername', 'TestEmail', 'Testhashedpassword');

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
```

### Procedures definition
All procedures definition can be found [here](./WebMonitoring/procedures)

#### get_daily_samples
Get samples out of each hour, for the last 24 hours.
This procedure has been generated with [this script](./WebMonitoring/generators/generate_samples_queries.py)
```sql
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

```


#### get_monthly_samples
Get samples each day, for the last 31 days.
This procedure has been generated with [this script](./WebMonitoring/generators/generate_samples_queries.py)
```sql
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

```


#### get_weekly_samples
Get samples each 6 hours, for the last 7 days.
This procedure has been generated with [this script](./WebMonitoring/generators/generate_samples_queries.py)
```sql
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

```



#### get_daily_samples_size
Get samples of size for each hour, for the last 24 hours.
This procedure has been generated with [this script](./WebMonitoring/generators/generate_samples_queries_size.py)
```sql
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
```


#### get_monthly_samples_size
Get samples of size for each day, for the last 31 days.
This procedure has been generated with [this script](./WebMonitoring/generators/generate_samples_queries_size.py)
```sql
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
    select HOUR(now()) INTO start_hour;
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

```


#### get_weekly_samples_size
Get samples of size each 6 hours, for the last 7 days.
This procedure has been generated with [this script](./WebMonitoring/generators/generate_samples_queries_size.py)
```sql
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

```



### Functions definition
All functions definition can be found [here](./WebMonitoring/functions)

#### resource_get_availability
Checks if a resource is up and running or is unavailable based on DB records.
```sql
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
```

#### resource_statistic_average_size
Returns average response size for ResourceMonitor.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_size;

CREATE FUNCTION resource_statistic_average_size() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_SIZE_ALL FLOAT;
    select AVG(ResponseSize) into AVERAGE_SIZE_ALL from PING;
    RETURN AVERAGE_SIZE_ALL;
END//

delimiter ;
```

#### resource_statistic_average_size_24
Returns average response size for ResourceMonitor for all records in the last 24 hours.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_size_24;

CREATE FUNCTION resource_statistic_average_size_24() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_SIZE_24 FLOAT;
    select AVG(ResponseSize) into AVERAGE_TIME_SIZE_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN AVERAGE_TIME_SIZE_24;
END//

delimiter ;
```

#### resource_statistic_size
Returns the sum of all response size for ResourceMonitor.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_size;

CREATE FUNCTION resource_statistic_size() RETURNS FLOAT
BEGIN
    DECLARE SIZE_ALL FLOAT;
    select SUM(ResponseSize) into SIZE_ALL from PING;
    RETURN SIZE_ALL;
END//

delimiter ;
```

#### resource_statistic_size_24
Returns the sum of all response size for ResourceMonitor for all records in the last 24 hours.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_size_24;

CREATE FUNCTION resource_statistic_size_24() RETURNS FLOAT
BEGIN
    DECLARE SIZE_24 FLOAT;
    select SUM(ResponseSize) into SIZE_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN SIZE_24;
END//

delimiter ;
```

#### resource_statistic_standard_deviation_size
Returns the population standard deviation of the recorded sizes for ResourceMonitor.

```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_size;

CREATE FUNCTION resource_statistic_standard_deviation_size() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV FLOAT;
    select STD(ResponseSize) into STD_DEV from PING;
    RETURN STD_DEV;
END//

delimiter ;
```

#### resource_statistic_standard_deviation_size_24
Returns the population standard deviation of the recorded sizes for ResourceMonitor  for all records in the last 24 hours.

```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_size_24;

CREATE FUNCTION resource_statistic_standard_deviation_size_24() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV_24 FLOAT;
    select STD(ResponseSize) into STD_DEV_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN STD_DEV_24;
END//

delimiter ;
```

#### resource_statistic_average_time
Returns average response time for ResourceMonitor for all records.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_time;

CREATE FUNCTION resource_statistic_average_time() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_ALL FLOAT;
    select AVG(ResponseTime) into AVERAGE_TIME_ALL from PING;
    RETURN AVERAGE_TIME_ALL;
END//

delimiter ;
```

#### resource_statistic_average_time_24
Returns average response time for ResourceMonitor for all records in the last 24 hours.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_average_time_24;

CREATE FUNCTION resource_statistic_average_time_24() RETURNS FLOAT
BEGIN
    DECLARE AVERAGE_TIME_ALL_24 FLOAT;
    select AVG(ResponseTime) into AVERAGE_TIME_ALL_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN AVERAGE_TIME_ALL_24;
END//

delimiter ;
```

#### resource_statistic_requests_time
Returns total number of requests stored in WebMonitoring.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_requests_time;

CREATE FUNCTION resource_statistic_requests_time() RETURNS INT
BEGIN
    DECLARE COUNT_REQUESTS INT;
    select count(*) total into COUNT_REQUESTS from PING;
    RETURN COUNT_REQUESTS;
END//

delimiter ;
```

#### resource_statistic_requests_time_24
Returns total number of requests stored in WebMonitoring in the last 24 hours.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_requests_time_24;

CREATE FUNCTION resource_statistic_requests_time_24() RETURNS INT
BEGIN
    DECLARE COUNT_REQUESTS_24 INT;
    select count(*) total into COUNT_REQUESTS_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN COUNT_REQUESTS_24;
END//

delimiter ;
```


#### resource_statistic_time
Returns the sum of all response time for ResourceMonitor for all records.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_time;

CREATE FUNCTION resource_statistic_time() RETURNS FLOAT
BEGIN
    DECLARE TIME_ALL FLOAT;
    select SUM(ResponseTime) into TIME_ALL from PING;
    RETURN TIME_ALL;
END//

delimiter ;
```

#### resource_statistic_time_24
Returns the sum of all response time for ResourceMonitor for all records in the last 24 hours.
```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_time_24;

CREATE FUNCTION resource_statistic_time_24() RETURNS FLOAT
BEGIN
    DECLARE TIME_24 FLOAT;
    select SUM(ResponseTime) into TIME_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN TIME_24;
END//

delimiter ;
```



### Triggers definition
All triggers definition can be found [here](./Login/triggers)

#### before_users_update
Audit all updates to USERS table inside DB

```sql
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
```

#### resource_statistic_standard_deviation_time
Returns the population standard deviation of the recorded times for ResourceMonitor for all records.

```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_time;

CREATE FUNCTION resource_statistic_standard_deviation_time() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV FLOAT;
    select STD(ResponseTime) into STD_DEV from PING;
    RETURN STD_DEV;
END//

delimiter ;
```

#### resource_statistic_standard_deviation_time_24
Returns the population standard deviation of the recorded times for ResourceMonitor for all records in the last 24 hours.

```sql
delimiter //

DROP FUNCTION IF EXISTS resource_statistic_standard_deviation_time_24;

CREATE FUNCTION resource_statistic_standard_deviation_time_24() RETURNS FLOAT
BEGIN
    DECLARE STD_DEV_24 FLOAT;
    select STD(ResponseTime) into STD_DEV_24 from PING  WHERE TIMESTAMP >= DATE_SUB(NOW(), INTERVAL 24 HOUR);
    RETURN STD_DEV_24;
END//

delimiter ;
```

#### before_users_delete
Audit all deletions to USERS table inside DB
```sql
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
```