-- Extracting Components of a Date
ALTER TABLE messy_indian_dataset
    ADD COLUMN day INT,
    ADD COLUMN month INT,
    ADD COLUMN year INT;

UPDATE messy_indian_dataset
    SET day = DAY(purchase_date),
        month = MONTH(purchase_date),
        year = YEAR(purchase_date);

SELECT * FROM messy_indian_dataset;


-- Adding a Column for Day of the Week
ALTER TABLE messy_indian_dataset
    ADD COLUMN day_of_week VARCHAR(10);

UPDATE messy_indian_dataset
    SET day_of_week = DAYNAME(purchase_date);
  
  
-- Adding a Column for Month Name
ALTER TABLE messy_indian_dataset
    ADD COLUMN month_name VARCHAR(10);

UPDATE messy_indian_dataset
    SET month_name = MONTHNAME(purchase_date);
    
    
-- 