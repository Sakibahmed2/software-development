-- Active: 1794030384000@@127.0.0.1@3306@dummydb
SELECT * FROM employees;

SELECT m.first_name, e.first_name FROM employees AS e
JOIN employees AS m ON e.employee_id = m.manager_id;

SELECT d.department_name FROM departments AS d
LEFT JOIN employees AS e
ON d.department_id = e.department_id
WHERE e.department_id IS NULL;

SELECT e.first_name, e.salary, (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id) - e.salary
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id;


SELECT department_name FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id
GROUP BY department_name
HAVING MIN(salary) > 5000 



