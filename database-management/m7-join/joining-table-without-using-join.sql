-- Active: 1794030384000@@127.0.0.1@3306@dummydb
SELECT * FROM employees;

SELECT * FROM departments;

SELECT employees.first_name, departments.department_name
FROM employees, departments 
WHERE employees.department_id = departments.department_id;