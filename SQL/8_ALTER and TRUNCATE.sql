CREATE DATABASE SCHOOL;
USE SCHOOL;
CREATE TABLE scholar(
roll INT PRIMARY KEY,
name VARCHAR(50),
grade VARCHAR(5),
marks INT
);

INSERT INTO scholar VALUES(1,"Aashish","A",70);
INSERT INTO scholar VALUES(5,"Sham","C",49);
INSERT INTO scholar VALUES(2,"Ram","F",12);
INSERT INTO scholar VALUES(3,"Krish","B",55);
INSERT INTO scholar VALUES(4,"Aashima","C",48);
INSERT INTO scholar VALUES(6,"Aman","A",77);

SELECT * FROM scholar;

ALTER TABLE scholar
ADD COLUMN age INT NOT NULL DEFAULT 20;

ALTER TABLE scholar
DROP COLUMN age;

ALTER TABLE scholar
RENAME TO shishya;

ALTER TABLE scholar
change COLUMN marks score INT;

ALTER TABLE scholar
MODIFY score VARCHAR(2);

TRUNCATE TABLE scholar;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM scholar
WHERE marks<65;

SELECT * FROM scholar;
