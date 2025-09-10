Exception Handling in SQL
Proper exception handling ensures that errors do not cause the application to crash and provides meaningful error messages.

-- 1. Handling Non-Existent Table Error
DELIMITER //
DROP PROCEDURE IF EXISTS handle_non_existent_table;
CREATE PROCEDURE handle_non_existent_table()
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        SELECT 'The table "non_existent_table" does not exist' AS message;
    END;
    SELECT * FROM non_existent_table;
END //
DELIMITER ;


CALL handle_non_existent_table();


-- 2. Handling Unique Constraint Violation
DELIMITER //
DROP PROCEDURE IF EXISTS handle_unique_violation;
CREATE PROCEDURE handle_unique_violation()
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        SELECT 'Duplicate restaurant ID or name found' AS message;
    END;
    INSERT INTO restaurants (id, name, city, rating)
    VALUES (211, 'Tandoori Hut', 'Bangalore', 4.3);
END //
DELIMITER ;


CALL handle_unique_violation();