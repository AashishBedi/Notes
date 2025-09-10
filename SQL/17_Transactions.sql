-- Database Creation
DROP TABLE IF EXISTS messy_indian_dataset;
CREATE TABLE IF NOT EXISTS messy_indian_dataset (
    id INT,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    email VARCHAR(100),
    phone_number VARCHAR(15),
    city VARCHAR(50),
    state VARCHAR(50),
    purchase_amount DECIMAL(10, 2),
    purchase_date DATE
);

INSERT INTO messy_indian_dataset (id, name, age, gender, email, phone_number, city, state, purchase_amount, purchase_date) VALUES
(1, 'Rajesh Patel', 30, 'Male', 'rajesh@example.com', '9876543210', 'Mumbai', 'Maharashtra', 1000.50, '2023-01-05'),
(2, 'Priya Sharma', 25, 'Female', 'priya@example.com', '9876543211', 'Delhi', 'Delhi', NULL, '2023-02-15'),
(3, 'Amit Kumar', 35, 'Male', 'amit@example.com', '9876543212', 'Bangalore', 'Karnataka', 750.25, '2023-03-25'),
(4, 'Ritu Singh', 28, 'Female', NULL, '9876543213', 'Kolkata', 'West Bengal', 1200.75, '2023-04-10'),
(5, 'Rajesh Patel', 30, 'Male', 'rajesh@example.com', '9876543210', 'Mumbai', 'Maharashtra', 1000.50, '2023-01-05'),
(6, 'Priya Sharma', 25, 'Female', 'priya@example.com', '9876543211', 'Delhi', 'Delhi', 800.00, '2023-02-15'),
(7, 'Amit Kumar', NULL, 'Male', 'amit@example.com', NULL, 'Bangalore', 'Karnataka', 750.25, '2023-03-25'),
(8, 'Ritu Singh', 28, 'Female', 'ritu@example.com', '9876543213', 'Kolkata', 'West Bengal', 1200.75, '2023-04-10'),
(9, 'Ankit Tiwari', 32, 'Male', 'ankit@example.com', '9876543214', 'Lucknow', 'Uttar Pradesh', 900.00, '2023-05-20'),
(10, 'Swati Gupta', 27, 'Female', 'swati@example.com', '9876543215', 'Jaipur', 'Rajasthan', 1500.00, NULL);


-- Example 1: Simple Transaction
START TRANSACTION;
UPDATE messy_indian_dataset SET purchase_amount = 1500 WHERE id = 1;
SELECT * FROM messy_indian_dataset;



-- Example 2: Transaction with Rollback
START TRANSACTION;
UPDATE messy_indian_dataset SET purchase_amount = 1400 WHERE id = 1;
SELECT * FROM messy_indian_dataset;
ROLLBACK;
SELECT * FROM messy_indian_dataset;



-- Example 3: Transaction with Commit
START TRANSACTION;
UPDATE messy_indian_dataset SET purchase_amount = 1300 WHERE id = 1;
SELECT * FROM messy_indian_dataset;
COMMIT;
SELECT * FROM messy_indian_dataset;



-- Example 4: Commit and Rollback
START TRANSACTION;
INSERT INTO messy_indian_dataset (id, name, age, gender, email, phone_number, city, state, purchase_amount, purchase_date) 
VALUES (11, 'Mahesh Patel', 30, 'Male', 'rajesh@example.com', '9876543210', 'Mumbai', 'Maharashtra', 1000.50, '2023-01-05');
SELECT * FROM messy_indian_dataset WHERE id = 11;
SELECT * FROM messy_indian_dataset;
COMMIT;
ROLLBACK;
SELECT * FROM messy_indian_dataset;



-- Example 5: Commit and Rollback with Multiple Commands
START TRANSACTION;
INSERT INTO messy_indian_dataset (id, name, age, gender, email, phone_number, city, state, purchase_amount, purchase_date) 
VALUES (12, 'Prakash', 30, 'Male', 'rajesh@example.com', '9876543210', 'Mumbai', 'Maharashtra', 1000.50, '2023-01-05');

INSERT INTO messy_indian_dataset (id, name, age, gender, email, phone_number, city, state, purchase_amount, purchase_date) 
VALUES (13, 'Aarti', 30, 'Female', 'rajesh@example.com', '9876543210', 'Mumbai', 'Maharashtra', 1000.50, '2023-01-05');

SELECT * FROM messy_indian_dataset;
COMMIT;
ROLLBACK;
SELECT * FROM messy_indian_dataset;



-- Example 6: Rollback with Multiple Commands
START TRANSACTION;
INSERT INTO messy_indian_dataset (id, name, age, gender, email, phone_number, city, state, purchase_amount, purchase_date) 
VALUES (14, 'Prakash', 30, 'Male', 'rajesh@example.com', '9876543210', 'Mumbai', 'Maharashtra', 1000.50, '2023-01-05');

INSERT INTO messy_indian_dataset (id, name, age, gender, email, phone_number, city, state, purchase_amount, purchase_date) 
VALUES (15, 'Aarti', 30, 'Female', 'rajesh@example.com', '9876543210', 'Mumbai', 'Maharashtra', 1000.50, '2023-01-05');

SELECT * FROM messy_indian_dataset;
ROLLBACK;
SELECT * FROM messy_indian_dataset;