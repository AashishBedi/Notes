
-- Finding Missing Values
SELECT * FROM messy_indian_dataset 
WHERE name IS NULL OR age IS NULL OR gender IS NULL OR email IS NULL OR city IS NULL OR
    phone_number IS NULL OR state IS NULL OR purchase_amount IS NULL OR purchase_date IS NULL;
    
-- Finding Rows Without Missing Values
SELECT * FROM messy_indian_dataset 
WHERE name IS NOT NULL AND age IS NOT NULL AND gender IS NOT NULL AND email IS NOT NULL AND city IS NOT NULL AND
    phone_number IS NOT NULL AND state IS NOT NULL AND purchase_amount IS NOT NULL AND purchase_date IS NOT NULL;
    
-- Saving a Clean Table
CREATE TABLE IF NOT EXISTS clean_table AS
SELECT * FROM messy_indian_dataset 
WHERE name IS NOT NULL AND age IS NOT NULL AND gender IS NOT NULL AND email IS NOT NULL AND city IS NOT NULL AND
    phone_number IS NOT NULL AND state IS NOT NULL AND purchase_amount IS NOT NULL AND purchase_date IS NOT NULL;

SELECT * FROM clean_table;

-- Filling Missing Values with Specific Values

-- 1. Filling Missing Age
UPDATE messy_indian_dataset SET age = COALESCE(age, 0);
SELECT * FROM messy_indian_dataset;

-- 2. Filling Other Null Values
UPDATE messy_indian_dataset 
SET
    name = COALESCE(name, 'Unknown'),
    gender = COALESCE(gender, 'Unknown'),
    email = COALESCE(email, 'Unknown'),
    phone_number = COALESCE(phone_number, 'Unknown'),
    state = COALESCE(state, 'Unknown'),
    purchase_date = COALESCE(purchase_date, '2023-01-01');

SELECT * FROM messy_indian_dataset;


-- Filling Missing Values with Calculated Values

-- 1. Filling Null Purchase Amount with Average Amount
UPDATE messy_indian_dataset
SET purchase_amount = (
    SELECT AVG(purchase_amount) FROM messy_indian_dataset
) WHERE purchase_amount IS NULL;

SELECT * FROM messy_indian_dataset;

-- 2. Filling Null City with Most Frequent City
UPDATE messy_indian_dataset 
SET city = (
    SELECT city FROM (
        SELECT city, COUNT(*) AS frequency 
        FROM messy_indian_dataset
        WHERE city IS NOT NULL
        GROUP BY city
        ORDER BY frequency DESC
        LIMIT 1
    ) AS subquery
) WHERE city IS NULL;

SELECT * FROM messy_indian_dataset;