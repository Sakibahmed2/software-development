SELECT
    e1.first_name AS Employee_1,
    e2.first_name AS Employee_2,
    e1.manager_id AS Manager_ID
FROM employees e1
INNER JOIN employees e2
    ON e1.manager_id = e2.manager_id
    AND e1.employee_id < e2.employee_id
WHERE e1.manager_id IS NOT NULL;

CREATE TABLE Employees (
    Employee_Id INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(100) NOT NULL,
    Last_Name VARCHAR(100) NOT NULL,
    Date_of_Birth DATE,
    Department_Id INT,
    Salary DECIMAL(10, 2)
);

CREATE TABLE Projects (
    Project_Id INT AUTO_INCREMENT PRIMARY KEY,
    Project_Name VARCHAR(150) NOT NULL,
    Start_Date DATE,
    End_Date DATE,
    Budget DECIMAL(12, 2)
);

CREATE TABLE Employee_Projects (
    Employee_Id INT,
    Project_Id INT,

    PRIMARY KEY (Employee_Id, Project_Id),

    FOREIGN KEY (Employee_Id)
        REFERENCES Employees(Employee_Id),

    FOREIGN KEY (Project_Id)
        REFERENCES Projects(Project_Id)
);


SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;

SELECT
    d.department_name,
    COUNT(e.employee_id) AS Total_Employees
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY d.department_id;

WITH AverageSalary AS (
    SELECT AVG(salary) AS avg_salary
    FROM employees
)
SELECT
    first_name,
    last_name,
    salary
FROM employees
WHERE salary > (
    SELECT avg_salary
    FROM AverageSalary
);



SELECT
    first_name,
    last_name,
    salary
FROM employees
WHERE salary < (
    SELECT salary
    FROM employees
    WHERE first_name = 'Steven'
      AND last_name = 'King'
);

SELECT
    d.department_name,
    e.first_name AS Manager_First_Name,
    e.last_name AS Manager_Last_Name
FROM departments d
LEFT JOIN employees e
    ON d.manager_id = e.employee_id
ORDER BY d.department_id;



SELECT DISTINCT
    l.city
FROM departments d
INNER JOIN locations l
    ON d.location_id = l.location_id
ORDER BY l.city;


















