-- Finding Outliers Based on Z-Score
SELECT *, 
       ABS(purchase_amount - AVG(purchase_amount) OVER()) / STDDEV(purchase_amount) OVER() AS 'z_score'
FROM messy_indian_dataset;

-- Removing Outliers Based on Specific Z-Score
SELECT * FROM
(
    SELECT *, 
           ABS(purchase_amount - AVG(purchase_amount) OVER()) / STDDEV(purchase_amount) OVER() AS 'z_score'
    FROM messy_indian_dataset
) AS sub_table 
WHERE sub_table.z_score < 3;