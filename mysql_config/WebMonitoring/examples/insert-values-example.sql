INSERT INTO USERS(LastName, FirstName, Username, Email, hashedpassword)
values ('TestLastName', 'TestFirstName', 'TestUsername', 'TestEmail', 'pbkdf2:sha256:150000$aLUr0Tku$b8bbd76305a65b5fde4c94a22017979c9f3918d251045b0029a07657c9c169fb');

INSERT INTO RESOURCE(Userid, ResourceName, Command)
values (1, 'https://github.com/raresraf/rafMetrics/projects/1', 'GET');

INSERT INTO PING(Resourceid, ResponseTime, ResponseSize)
values (1, 0.906846, 86217);

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'GitHub: rafMetrics Projects/1', 'https://github.com/raresraf/rafMetrics/projects/1');

INSERT INTO WEBSITES(Userid, WebsiteName, WebsiteUrl)
values (1, 'Google: default website', 'https://google.com');

INSERT INTO WEBSITES_METRICS(Websiteid, TotalTime)
values (1, 2.198);

INSERT INTO REQUESTS(Metricid, serverIPAddress, pageRef, startedDateTime, time, responseStatus, headersSize, bodySize)
VALUES (1, '185.199.111.154', 'https://github.com/raresraf/rafMetrics/projects/1', '2019-10-22T13:38:31.878Z',178, 200, 671, 462);

INSERT INTO TIMINGS(Requestid, Receive, Send, SSLTime, Connect, DNS, Blocked, Wait)
VALUES (1, 0, 2, 99, 141, 0, 0, 32);



-- unknown
INSERT INTO RESOURCE(Userid, ResourceName, Command)
VALUES (1, 'https://g1thub.com/raresraf/rafMetrics', 'GET');