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