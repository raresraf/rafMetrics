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

