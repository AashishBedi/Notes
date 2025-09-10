-- Functions in SQL
A function in SQL is a routine that can accept parameters, perform calculations or operations, and return a single value. 
Functions are typically used for operations that need to be executed frequently, such as calculations or data transformations.

-- Example 1: Function to Calculate Age
DROP FUNCTION IF EXISTS CalculateAge;
DELIMITER //
CREATE FUNCTION CalculateAge(birthdate DATE) RETURNS INT
DETERMINISTIC
BEGIN 
    DECLARE age INT;
    SET age = YEAR(CURDATE()) - YEAR(birthdate);
    RETURN age;
END //
DELIMITER ;

SELECT CalculateAge('1990-05-15') AS age;


-- Example 2: Function to Calculate Tax
DROP FUNCTION IF EXISTS CalculateTax;
DELIMITER //
CREATE FUNCTION CalculateTax(amount DECIMAL(10,2), tax_rate DECIMAL(5,2)) RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN 
    DECLARE tax DECIMAL(10,2);
    SET tax = amount * (tax_rate / 100);
    RETURN tax;
END //
DELIMITER ;

SELECT CalculateTax(1000.15, 18) AS tax_amount;


-- Example 3: Function to Categorize Age
DROP FUNCTION IF EXISTS GetAgeCategory;
DELIMITER //
CREATE FUNCTION GetAgeCategory(age INT) RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN 
    DECLARE category VARCHAR(20);
    IF age < 18 THEN
        SET category = 'child';
    ELSEIF age BETWEEN 18 AND 65 THEN
        SET category = 'adult';
    ELSE
        SET category = 'senior';
    END IF;
    RETURN category;
END //
DELIMITER ;

SELECT GetAgeCategory(19) AS category;



-- Procedures in SQL
A procedure in SQL, also known as a stored procedure, is a set of SQL statements that can perform a variety of tasks. 
Unlike functions, procedures can perform actions that affect the database state and may or may not return values. 
Procedures are typically used for more complex operations that require multiple steps or involve conditional logic.

-- Example 4: Creating Your First Procedure
DROP PROCEDURE IF EXISTS GetUserByID;
DELIMITER //
CREATE PROCEDURE GetUserByID(IN userID INT)
BEGIN
    SELECT * FROM messy_indian_dataset WHERE id = userID;
END //
DELIMITER ;

CALL GetUserByID(1);


-- Example 5: Procedure to Update Purchase Amount by Percentage
DROP PROCEDURE IF EXISTS UpdatePurchaseAmount;
DELIMITER //
CREATE PROCEDURE UpdatePurchaseAmount(IN percentage DECIMAL(5,2))
BEGIN
    UPDATE messy_indian_dataset
    SET purchase_amount = purchase_amount * (1 + percentage / 100);
    SELECT * FROM messy_indian_dataset;
END //
DELIMITER ;

CALL UpdatePurchaseAmount(10);


-- Example 6: Deleting Low-Rated Restaurants and Logging
CREATE TABLE IF NOT EXISTS deleted_rest_log(
    id INT,
    name VARCHAR(255),
    rating DECIMAL(3,2),
    deletion_time TIMESTAMP
);

DROP PROCEDURE IF EXISTS delete_low_rate_rest;
DELIMITER //
CREATE PROCEDURE delete_low_rate_rest(min_rating DECIMAL(3,2))
BEGIN
    INSERT INTO deleted_rest_log (id, name, rating, deletion_time)
    SELECT id, name, rating, NOW() FROM swiggy.restaurants
    WHERE rating < min_rating;
    
    DELETE FROM swiggy.restaurants
    WHERE rating < min_rating;
END //
DELIMITER ; 

CALL delete_low_rate_rest(3.0);

SELECT * FROM swiggy.restaurants;