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

INSERT INTO USERS(LastName, FirstName, Username, Email, hashedpassword)
    values ('TestLastName', 'TestFirstName', 'TestUsername', 'TestEmail', 'Testhashedpassword');


CREATE table RESOURCE (
                          Resourceid int NOT NULL AUTO_INCREMENT,
                          Userid int NOT NULL,
                          ResourceName varchar(255) NOT NULL,
                          Command varchar(255) NOT NULL,
                          FirstAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                          PRIMARY KEY (Resourceid),
                          FOREIGN KEY (Userid) REFERENCES USERS(Userid)
);

INSERT INTO RESOURCE(Userid, ResourceName, Command)
    values (1, 'https://github.com/raresraf/rafMetrics/projects/1', 'GET');


CREATE table PING (
                          Pingid int NOT NULL AUTO_INCREMENT,
                          Resourceid int NOT NULL,
                          ResponseTime double NOT NULL,
                          ResponseSize int NOT NULL,
                          Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                          PRIMARY KEY (Pingid),
                          FOREIGN KEY (Resourceid) REFERENCES RESOURCE(Resourceid)
);

INSERT INTO PING(Resourceid, ResponseTime, ResponseSize)
    values (1, 0.906846, 86217);


CREATE table WEBSITES (
                          Websiteid int NOT NULL AUTO_INCREMENT,
                          Userid int NOT NULL,
                          WebsiteName varchar(255) NOT NULL,
                          WebsiteUrl varchar(255) UNIQUE,
                          FirstAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                          PRIMARY KEY (Websiteid),
                          FOREIGN KEY (Userid) REFERENCES USERS(Userid)
);

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
    values (1, 'GitHub: rafMetrics Projects/1', 'https://github.com/raresraf/rafMetrics/projects/1');
INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
    values (1, 'Google: default website', 'https://google.com');


CREATE table WEBSITES_METRICS (
                          Metricid int NOT NULL AUTO_INCREMENT,
                          Websiteid int NOT NULL,
                          TotalTime double,
                          Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                          PRIMARY KEY (Metricid),
                          FOREIGN KEY (Websiteid) REFERENCES WEBSITES(Websiteid)
);

INSERT INTO WEBSITES_METRICS(Websiteid, TotalTime)
    values (1, 2.198);


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

INSERT INTO REQUESTS(Metricid, serverIPAddress, pageRef, startedDateTime, time, responseStatus, headersSize, bodySize)
VALUES (1, '185.199.111.154', 'https://github.com/raresraf/rafMetrics/projects/1', '2019-10-22T13:38:31.878Z',178, 200, 671, 462);


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


INSERT INTO TIMINGS(Requestid, Receive, Send, SSLTime, Connect, DNS, Blocked, Wait)
VALUES (1, 0, 2, 99, 141, 0, 0, 32);