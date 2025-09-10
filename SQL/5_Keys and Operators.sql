CREATE DATABASE CLG;
USE CLG;

CREATE TABLE stu(
rno INT PRIMARY KEY,
name VARCHAR(50),
marks INT NOT NULL,
grade VARCHAR(1)
);

INSERT INTO stu(rno, name, marks, grade) VALUES
(5,"ASI",56,"A"),
(6,"AMI",32,"D"),
(7,"BHIM",01,"F");
SELECT name,marks from stu;
SELECT * from stu;
SELECT * from stu WHERE marks>50;
SELECT * from stu WHERE marks>50 OR name = "ASI";
SELECT * from stu WHERE marks BETWEEN 50 AND 60;
SELECT * from stu WHERE city in ("DELHI","PUNE");
SELECT * from stu WHERE city NOT IN ("DELHI","PUNE");
SELECT * from stu LIMIT 3;
SELECT * from stu;
SELECT * from stu ORDER BY name ASC;
SELECT * from stu ORDER BY name DESC LIMIT 3;
SELECT max(marks) from stu;
-- can use min, count, avg, sum

SELECT city, count(name) FROM stu GROUP BY city;
SELECT city, avg(marks) from stu GROUP BY city ORDER BY avg(marks) ASC;