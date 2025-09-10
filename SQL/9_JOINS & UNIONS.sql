CREATE DATABASE DB;
USE DB;

CREATE TABLE student(
stu_id INT PRIMARY KEY,
name VARCHAR(20)
);
CREATE TABLE course(
stu_id INT PRIMARY KEY,
course VARCHAR(50)
);

INSERT INTO student(stu_id,name) VALUES
(101,"ADAM"),
(102,"BOB"),
(103,"CASEY");

INSERT INTO course(stu_id,course) VALUES
(102,"ENGLISH"),
(105,"MATH"),
(103,"SCIENCE"),
(107,"CSE");

-- INNER JOIN
/*
SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;
*/
SELECT * FROM student as s
INNER JOIN course as c
ON s.stu_id = c.stu_id;


-- LEFT JOIN
/*
SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;
*/
SELECT * FROM student as s
LEFT JOIN course as c
ON s.stu_id = c.stu_id;


-- RIGHT JOIN
/*
SELECT column(s)
FROM tableA
RIGHT JOIN tableB
ON tableA.col_name = tableB.col_name;
*/
SELECT * FROM student as s
RIGHT JOIN course as c
ON s.stu_id = c.stu_id;


-- FULL JOIN
/*
SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name
UNION
SELECT * FROM tableA
RIGHT JOIN tableB
ON tableA.col_name = tableB.col_name
;
*/
SELECT * FROM student as s
LEFT JOIN course as c
ON s.stu_id = c.stu_id
UNION
SELECT * FROM student as s
RIGHT JOIN course as c
ON s.stu_id = c.stu_id;

-- LEFT EXCLUSIVE JOIN
SELECT * FROM student as s
LEFT JOIN course as c
ON s.stu_id = c.stu_id
WHERE c.stu_id IS NULL;

-- RIGHT EXCLUSIVE JOIN
SELECT * FROM student as s
RIGHT JOIN course as c
ON s.stu_id = c.stu_id
WHERE s.stu_id IS NULL;


CREATE TABLE emp(
id INT PRIMARY KEY,
name VARCHAR(50),
manager_id INT
);

INSERT INTO emp(id,name, manager_id) VALUES
(101,"ADAM",103),
(102,"BOB",104),
(103,"CASEY",NULL),
(104,"DONALD",103);

-- SELF JOIN
SELECT * FROM emp as a
JOIN emp as b
ON a.id = b.manager_id;



SELECT a.name as manager_name, b.name
FROM emp as a
JOIN emp as b
ON a.id = b.manager_id;


-- UNION
SELECT name FROM emp
UNION
SELECT name FROM emp;


SELECT name FROM emp
UNION ALL
SELECT name FROM emp;
