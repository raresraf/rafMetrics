# DB setup
Follow the following steps to setup the DB
## MySQL docker image
[mysql:5.6](https://hub.docker.com/_/mysql)
## MySQL deployment in Kubernetes
[Deployment config file](../mysql/deploy/mysql-deployment.yaml)

## MySQL init
### Create tables
#### For Platform:
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
```

### Populate tables
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

### Functions definition

### Triggers definition
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