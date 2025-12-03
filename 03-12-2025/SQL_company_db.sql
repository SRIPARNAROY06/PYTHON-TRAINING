CREATE DATABASE company_db;
USE company_db;

CREATE TABLE departments(
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50),
location VARCHAR(50)
);

CREATE TABLE employees(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
email VARCHAR(50),
salary INT,
dept_id INT NULL
);

INSERT INTO departments (dept_id, dept_name, location)

VALUES

(10, 'HR', 'Mumbai'),

(20, 'Finance', 'Delhi'),

(30, 'IT', 'Bangalore'),

(40, 'Marketing', 'Chennai'),

(50, 'Admin', 'Hyderabad');   -- no employees for dept 50
 
 
INSERT INTO employees (emp_id, emp_name, email, salary, dept_id)

VALUES

(101, 'Aisha Khan', 'aisha@company.com', 60000, 10),

(102, 'Rahul Sharma', 'rahul@company.com', 72000, 20),

(103, 'Meera Iyer', 'meera@company.com', 50000, 30),

(104, 'Imran Ali', 'imran@company.com', 65000, NULL),  -- no department

(105, 'Sanjay Patel', 'sanjay@company.com', 45000, NULL), -- no department

(106, 'David John', 'david@company.com', 90000, 40);
 
 
SELECT e.emp_id, e.emp_name, d.dept_name, d.location
FROM employees e
LEFT JOIN departments d
ON e.dept_id=d.dept_id

UNION

SELECT e.emp_id, e.emp_name, d.dept_name, d.location
FROM employees e
RIGHT JOIN departments d
ON e.dept_id=d.dept_id;

SELECT e.emp_name, d.dept_name
FROM employees e
CROSS JOIN departments d;






 