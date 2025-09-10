-- 1: Rank Every Restaurant by Cost (Descending Order)
SELECT *, RANK() OVER(ORDER BY cost DESC) AS 'rank'
FROM restaurants;

-- Rank Every Restaurant by Rating Count (Descending Order)
SELECT *, RANK() OVER(ORDER BY rating_count DESC) AS 'rank'
FROM restaurants;

-- Rank Every Restaurant by Cost Within Each City
SELECT *, RANK() OVER(PARTITION BY city ORDER BY cost DESC) AS 'rank'
FROM restaurants;

-- Rank Every Restaurant by Cost with Dense Ranking Within Each City
SELECT *,
       RANK() OVER(ORDER BY cost DESC) AS 'rank',
       DENSE_RANK() OVER(ORDER BY cost DESC) AS 'dense_rank'
FROM restaurants;

-- Row Number Every Restaurant by Cost Within Each City
SELECT *,
       RANK() OVER(ORDER BY cost DESC) AS 'rank',
       DENSE_RANK() OVER(ORDER BY cost DESC) AS 'dense_rank',
       ROW_NUMBER() OVER(ORDER BY cost DESC) AS 'row_number'
FROM restaurants;

-- Rank Every Restaurant by Cost Within Each City with City Name Prefix
SELECT *,
       CONCAT(city, ' - ', ROW_NUMBER() OVER(PARTITION BY city ORDER BY cost DESC)) AS 'rank'
FROM restaurants;

--  Find Top 5 Restaurants of Every City by Revenue
SELECT *
FROM (
    SELECT *,
           cost * rating_count AS 'revenue',
           ROW_NUMBER() OVER(PARTITION BY city ORDER BY cost * rating_count DESC) AS 'rank'
    FROM restaurants
) AS t
WHERE t.rank <= 5;

-- Find Top 5 Restaurants of Every Cuisine by Revenue
SELECT *
FROM (
    SELECT *,
           cost * rating_count AS 'revenue',
           ROW_NUMBER() OVER(PARTITION BY cuisine ORDER BY cost * rating_count DESC) AS 'rank'
    FROM restaurants
) AS t
WHERE t.rank <= 5;