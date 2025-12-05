CREATE DATABASE IF NOT EXISTS employee_mgmt;
USE employee_mgmt;

CREATE TABLE IF NOT EXISTS employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept VARCHAR(100),
    role VARCHAR(100),
    salary DECIMAL(12,2) NOT NULL,
    join_date DATE DEFAULT (CURRENT_DATE)
);

INSERT INTO employees (name, dept, role, salary, join_date) VALUES
('Ananya Gupta', 'HR', 'HR Executive', 35000, '2024-03-01'),
('Rahul Sharma', 'IT', 'Developer', 65000, '2023-11-15'),
('Priya Sen', 'Finance', 'Accounts Manager', 80000,'2025-10-27'),
('Sriparna Roy','Consulting','Software Engineer',35000,'2025-11-01');


