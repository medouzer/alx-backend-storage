-- Email validation to sent
CREATE TRIGGER reset 
BEFORE UPDATE
ON users
FOR EACH ROW
IF NEW.email != OLD.email THEN
	SET NEW.valid_email = 0;
END IF;
