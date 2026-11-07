-- Active: 1794030384000@@127.0.0.1@3306@test
CREATE TABLE Employee(
	empId CHAR(6) PRIMARY KEY,
    empName VARCHAR(50) NOT NULL,
    joiningYear INT NOT NULL,
    birthday INT,
    designation VARCHAR(50) NOT NULL,
    salary INT,
    CONSTRAINT check_birthday_yr CHECK(birthday < 2000)
);

INSERT INTO Employee
(empId, empName, joiningYear, birthday, designation, salary)
VALUES
('EMP001', 'Sakib Ahmed', 2020, 1998, 'Software Engineer', 45000),
('EMP002', 'Rahim Hasan', 2019, 1995, 'Backend Developer', 55000),
('EMP003', 'Karim Uddin', 2021, 1997, 'Frontend Developer', 40000),
('EMP004', 'Tanvir Islam', 2018, 1994, 'Project Manager', 75000),
('EMP005', 'Nayeem Ahmed', 2022, 1999, 'Junior Developer', 30000),
('EMP006', 'Sadia Rahman', 2020, 1996, 'UI/UX Designer', 42000),
('EMP007', 'Hasan Mahmud', 2017, 1992, 'Senior Developer', 85000),
('EMP008', 'Nusrat Jahan', 2023, 1998, 'HR Manager', 38000),
('EMP009', 'Fahim Hossain', 2019, 1993, 'Database Administrator', 60000),
('EMP010', 'Anika Akter', 2021, 1997, 'QA Engineer', 35000),
('EMP011', 'Mehedi Hasan', 2016, 1991, 'System Analyst', 80000),
('EMP012', 'Tamim Iqbal', 2022, 1999, 'Web Developer', 32000),
('EMP013', 'Shakil Ahmed', 2018, 1995, 'DevOps Engineer', 65000),
('EMP014', 'Mim Akter', 2020, 1996, 'Content Writer', 30000),
('EMP015', 'Arafat Rahman', 2015, 1990, 'Software Architect', 95000),
('EMP016', 'Jannat Islam', 2023, 1999, 'Junior Designer', 28000),
('EMP017', 'Rifat Hossain', 2019, 1994, 'Network Engineer', 50000),
('EMP018', 'Sumaiya Akter', 2021, 1998, 'Data Analyst', 48000),
('EMP019', 'Imran Khan', 2017, 1993, 'Security Engineer', 70000),
('EMP020', 'Mahir Hasan', 2022, 1997, 'Technical Support Engineer', 35000);

SELECT * FROM employee where salary > 50000;

SELECT empName, salary FROM employee WHERE joiningYear > 2000;


-- Find employee who's designation is software engineer
SELECT * FROM employee 
    WHERE designation = "software engineer";


-- Find employee order by salary
SELECT * FROM employee ORDER BY salary DESC;

-- Find top 5 highest paid employee
SELECT * FROM employee ORDER BY salary DESC LIMIT 5;

-- Cont total employee
SELECT COUNT(*) FROM employee;

-- Calculate total salary of employees
SELECT SUM(salary) FROM employee;

-- Count employee in each designation
SELECT designation, COUNT(*) 
    FROM employee
    GROUP BY designation;

-- Find designation with avg salary grater then 40000
SELECT designation, AVG(salary)
    FROM employee
    GROUP BY designation
    HAVING AVG(salary) > 40000;