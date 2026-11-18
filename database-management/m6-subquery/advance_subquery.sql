-- Active: 1794030384000@@127.0.0.1@3306@dummydb

-- Bad way to get second highest salary
SELECT * FROM employees
WHERE salary = (
    SELECT DISTINCT salary FROM employees
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
);


-- Good way

SELECT * FROM employees 
WHERE salary = (
    SELECT MAX(salary) FROM employees
    WHERE salary < ( SELECT MAX(salary) FROM employees)
);


SELECT * FROM employees AS emp
WHERE salary > (
    SELECT salary FROM employees AS mgr
    WHERE emp.manager_id = mgr.employee_id
);

SELECT * FROM employees AS emp
WHERE job_id = (
    SELECT job_id FROM employees AS mgr
    WHERE emp.employee_id = mgr.employee_id
);


WITH EMP_TEMP AS (
    SELECT * FROM employees
    LIMIT 5
)

SELECT * FROM `EMP_TEMP`;