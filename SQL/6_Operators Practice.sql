CREATE DATABASE COMPANY;
USE COMPANY;

CREATE TABLE cs(
id INT PRIMARY KEY,
cus VARCHAR(50),
mode VARCHAR(20),
city VARCHAR(100),
amt INT NOT NULL
);

INSERT into cs(id,cus,mode,city,amt) Values
(101,"Olive","Netbank","Auckland",10000),
(102,"Hame","Netbank","Texas",5000),
(103,"Love","Credit Card","Melbourne",8500),
(104,"Olivia","Cash","Auckland",5600),
(105,"Shane","UPI","Auckland",4000),
(106,"Abu Bakr","UPI","Sydney",5500),
(107,"John Sol","Cash","Toronto",6700),
(108,"Nick Colson","Netbank","New Papua Guinea",12000),
(109,"Ajaz","Cash","Auckland",1500),
(110,"Akash","Credit Card","Melbourne",500);
-- WHERE is used for rows whereas HAVING is used for groups
SELECT mode,count(cus) from cs group by mode;
SELECT count(mode) from cs group by mode;
SELECT mode,count(mode) from cs group by mode;

SELECT city,count(cus) FROM cs GROUP BY city;
SELECT city,count(cus) FROM cs GROUP BY city HAVING max(amt)>5000;
SELECT city,count(cus) FROM cs GROUP BY city HAVING max(amt)>8000;
