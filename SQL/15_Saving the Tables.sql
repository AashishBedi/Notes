-- Creating Temporary Tables:
-- Temporary tables (temp_restaurants) are useful for storing data temporarily within a session, 
-- facilitating complex queries without altering the original dataset.

CREATE TEMPORARY TABLE temp_restaurants AS SELECT * FROM restaurants;
SELECT * FROM temp_restaurants;



-- Aggregating Data in Temporary Tables:
-- Temporary tables (temp_city_statistics) aggregate data for statistical analysis, 
-- providing insights without modifying the primary dataset.

CREATE TEMPORARY TABLE temp_city_statistics AS 
    SELECT city, AVG(rating) AS avg_rating, COUNT(*) AS num_of_restaurants 
    FROM restaurants 
    GROUP BY city;
SELECT * FROM temp_city_statistics;



-- Using Aliases for Clarity:
-- Aliases (rest) improve query readability and manageability, 
-- especially in complex queries involving self-referencing or aggregated data.

SELECT rest.city, AVG(rest.cost) AS avg_cost 
FROM restaurants AS rest 
GROUP BY rest.city;



-- Filtering Data with Subqueries:
-- Subqueries help filter data (restaurants) based on conditions derived from the same dataset,
-- enhancing query flexibility and performance.

SELECT rest.*
FROM restaurants AS rest 
WHERE rest.rating > (SELECT AVG(rating) FROM restaurants WHERE city = rest.city);