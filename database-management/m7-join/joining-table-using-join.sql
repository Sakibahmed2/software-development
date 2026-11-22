-- Active: 1794030384000@@127.0.0.1@3306@dummydb
SELECT emp.first_name, dept.department_name FROM employees AS emp
JOIN departments AS dept ON emp.department_id = dept.department_id;

SELECT emp.first_name, dept.department_name FROM employees AS emp
JOIN departments AS dept USING(department_id);

