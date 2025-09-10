-- Finding Unique Values Based on ID
SELECT id
FROM messy_indian_dataset
GROUP BY id
ORDER BY id;

-- Finding Unique Values Based on Name
SELECT name
FROM messy_indian_dataset
GROUP BY name
ORDER BY name;

-- Finding Unique Values Based on ID Using Rank
SELECT id, name, age, gender, email, phone_number, city, state, purchase_amount, purchase_date 
FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY id ORDER BY id) AS 'rank' 
    FROM messy_indian_dataset
) AS subtable
WHERE subtable.rank = 1;

-- Finding Unique Values Based on Multiple Columns
SELECT id, name, age, gender, email, phone_number, city, state, purchase_amount, purchase_date 
FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY id, name ORDER BY id) AS 'rank' 
    FROM messy_indian_dataset
) AS subtable
WHERE subtable.rank = 1;