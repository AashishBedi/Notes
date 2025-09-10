-- Creating a Basic View

DROP VIEW IF EXISTS rest;
CREATE VIEW rest AS (
    SELECT name, city, rating, rating_count AS 'orders', 
           cuisine, cost, cost * rating_count AS 'revenue' 
    FROM restaurants
);
SELECT * FROM rest;

-- Creating a User View

DROP VIEW IF EXISTS user_view;
CREATE VIEW user_view AS (
    SELECT name, city, rating, rating_count AS 'orders', 
           cuisine, cost 
    FROM restaurants
);
SELECT * FROM user_view;

--  View for Specific Cuisine

DROP VIEW IF EXISTS rest_of_sweet_dishes;
CREATE VIEW rest_of_sweet_dishes AS (
    SELECT * 
    FROM restaurants 
    WHERE cuisine IN ('Sweets', 'Desserts', 'Bakery', 'Ice Cream')
);
SELECT * FROM rest_of_sweet_dishes;

-- View for Top 100 Restaurants

DROP VIEW IF EXISTS top_100;
CREATE VIEW top_100 AS (
    SELECT * 
    FROM restaurants 
    ORDER BY rating_count DESC 
    LIMIT 100
);
SELECT * FROM top_100;

-- View for Restaurants with At Least 100 Visitors

DROP VIEW IF EXISTS least_100;
CREATE VIEW least_100 AS (
    SELECT * 
    FROM restaurants 
    ORDER BY rating_count ASC 
    LIMIT 100
);
SELECT * FROM least_100;

--  View for Top 1000 Most Expensive Restaurants

DROP VIEW IF EXISTS top_1000_exp;
CREATE VIEW top_1000_exp AS (
    SELECT * 
    FROM restaurants 
    ORDER BY cost DESC 
    LIMIT 1000
);
SELECT * FROM top_1000_exp;

--  Top-Rated Restaurants in Each City

DROP VIEW IF EXISTS top_rated_rest_per_city;
CREATE VIEW top_rated_rest_per_city AS (
    SELECT * 
    FROM ( 
        SELECT *,  ROW_NUMBER() OVER(PARTITION BY city ORDER BY rating * rating_count DESC) AS 'rank' 
        FROM restaurants
    ) AS ranked_table
    WHERE ranked_table.rank = 1
);
SELECT * FROM top_rated_rest_per_city;