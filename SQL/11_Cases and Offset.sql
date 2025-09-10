create database Employees;
use Employees;

CREATE TABLE emp (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT NOT NULL,
    department VARCHAR(50)
);

INSERT INTO emp VALUES(1,"AASHISH",20,"Sales");
INSERT INTO emp VALUES(2,"AASHUTOSH",38,"Marketing");
INSERT INTO emp VALUES(3,"AASHIMA",42,"Sales");
INSERT INTO emp VALUES(4,"AASHISHDEEP",33,"HR");
INSERT INTO emp VALUES(5,"VIKAS",20,"Sales");
INSERT INTO emp VALUES(6,"VIRAT",27,"Marketing");
INSERT INTO emp VALUES(7,"RIDHI",29,"HR");
INSERT INTO emp VALUES(8,"KHUSHI",25,"Finance");
INSERT INTO emp VALUES(9,"MEHAK",24,"Finance");
INSERT INTO emp VALUES(10,"AKASH",24,"Marketing");
INSERT INTO emp VALUES(11,"TANVI",24,"Sales");
INSERT INTO emp VALUES(12,"NITISH",43,"Law");
SELECT * FROM emp;

select * from emp limit 5 offset 3;

select name,
case department
    when 'Sales' then 'Sales Team'
    else 'other'
end as emp_name from emp;




select name,
case 
    when age<30 then
         case
             when department = 'Sales' then 'Jr Sales'
             else 'Junior'
		 end
     when age>=30 and age<40 then 'Middle'
     else 'Senior'
end as emp_name from emp;