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