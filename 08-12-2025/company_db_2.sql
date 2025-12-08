CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

-- 2) Parent: employees
CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    role VARCHAR(50),
    salary INT DEFAULT 0
);

-- 3) Child: departments (references employees.id as the department head/owner)
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50) DEFAULT 'HQ',
    head_emp_id INT,  -- FK to employees(id)
    CONSTRAINT fk_departments_head
        FOREIGN KEY (head_emp_id) REFERENCES employees(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL,
    UNIQUE KEY uniq_dept_name (dept_name)
);

-- 4) Insert employees (parent rows)
INSERT INTO employees (name, role, salary) VALUES
('Alice Johnson',  'Developer',        60000),
('Bob Smith',      'Designer',         55000),
('Charlie Brown',  'Manager',          75000),
('Diana Prince',   'HR Specialist',    50000),
('Ethan Hunt',     'QA Engineer',      52000),
('Fiona Gallagher','Product Designer', 59000);

-- 5) Insert departments (child rows)
-- Map department heads to employee IDs inserted above:
-- Alice=1, Bob=2, Charlie=3, Diana=4, Ethan=5, Fiona=6
INSERT INTO departments (dept_name, location, head_emp_id) VALUES
('Engineering',      'New York',       1),  -- Head: Alice
('Design',           'San Francisco',  2),  -- Head: Bob
('Management',       'Boston',         3),  -- Head: Charlie
('Human Resources',  'Chicago',        4),  -- Head: Diana
('Quality Assurance','Austin',         5);  -- Head: Ethan



