-- PING
SHOW CREATE TABLE PING;
alter table PING drop foreign key PING_ibfk_1;
alter table PING add foreign key (Resourceid) references RESOURCE(Resourceid) on DELETE CASCADE;

-- RESOURCE
SHOW CREATE TABLE RESOURCE;
alter table RESOURCE drop foreign key RESOURCE_ibfk_1;
alter table RESOURCE add foreign key (Userid) references USERS(Userid) on DELETE CASCADE;

-- TIMINGS
SHOW CREATE TABLE TIMINGS;
alter table TIMINGS drop foreign key TIMINGS_ibfk_1;
alter table TIMINGS add foreign key (Requestid) references REQUESTS(Requestid) on DELETE CASCADE;

-- REQUESTS
SHOW CREATE TABLE REQUESTS;
alter table REQUESTS drop foreign key REQUESTS_ibfk_1;
alter table REQUESTS add foreign key (Metricid) references WEBSITES_METRICS(Metricid) on DELETE CASCADE;

-- WEBSITES
SHOW CREATE TABLE WEBSITES;
alter table WEBSITES drop foreign key WEBSITES_ibfk_1;
alter table WEBSITES add foreign key (Userid) references USERS(Userid) on DELETE CASCADE;

