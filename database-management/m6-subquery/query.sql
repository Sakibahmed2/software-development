-- Active: 1794030384000@@127.0.0.1@3306@dummydb


SELECT * FROM employees
WHERE salary < (
    SELECT salary FROM employees
    WHERE employee_id = 100
);

SELECT * FROM employees
WHERE salary = (
    SELECT MAX(salary) FROM employees
);