CREATE DATABASE UNI;
USE uni;

CREATE TABLE stu(
roll INT PRIMARY KEY,
name VARCHAR(50),
grade VARCHAR(5),
marks INT
);

INSERT INTO stu VALUES(101,"Anil","A",70);
INSERT INTO stu VALUES(102,"Bhumika","C",49);
INSERT INTO stu VALUES(103,"Chetan","F",12);
INSERT INTO stu VALUES(104,"Dhruv","B",55);
INSERT INTO stu VALUES(105,"Emanuel","C",48);
INSERT INTO stu VALUES(106,"Farah","A",77);


-- SUBQUERIES with WHERE
SELECT AVG(marks) FROM stu;
SELECT name, marks FROM stu WHERE marks>51;
SELECT name, marks FROM stu WHERE marks>(SELECT AVG(marks) FROM stu);


SELECT roll FROM stu WHERE roll%2 = 0;
SELECT name,roll FROM stu WHERE roll IN (SELECT roll FROM stu WHERE roll%2 = 0);

-- SUBQUERIES with FROM
SELECT MAX(marks) FROM(SELECT * FROM stu WHERE city = "Delhi");



-- VIEWS
CREATE VIEW view1 AS
SELECT roll, name, marks FROM stu;

SELECT * FROM view1
WHERE marks>=70;

drop view view1;