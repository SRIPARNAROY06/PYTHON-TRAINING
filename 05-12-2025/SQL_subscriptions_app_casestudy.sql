CREATE DATABASE IF NOT EXISTS subscription_app;
USE subscription_app;
 
DROP TABLE IF EXISTS subscriptions;
 
CREATE TABLE subscriptions (
  sub_id INT PRIMARY KEY,
  customer_name VARCHAR(50) NOT NULL,
  start_date DATE NOT NULL,
  expiry_date DATE NOT NULL,
  created_at DATETIME NOT NULL,
  plan_type VARCHAR(20) NOT NULL  -- Monthly, Quarterly, Yearly
);
 

INSERT INTO subscriptions (sub_id, customer_name, start_date, expiry_date, created_at, plan_type) VALUES
  (1,  'Aisha Khan',   '2024-12-15', '2025-01-15', '2024-12-15 10:30:00', 'Monthly'),
  (2,  'Rahul Sharma', '2025-01-05', '2025-02-05', '2025-01-05 09:45:00', 'Monthly'),
  (3,  'Imran Ali',    '2025-02-10', '2025-03-10', '2025-02-10 14:12:00', 'Monthly'),
  (4,  'Meera Iyer',   '2025-03-01', '2025-04-01', '2025-03-01 17:05:00', 'Monthly'),
  (5,  'Sanjay Patel', '2025-02-20', '2025-05-21', '2025-02-20 13:00:00', 'Quarterly'),
  (6,  'Neha Gupta',   '2024-06-10', '2025-06-10', '2024-06-10 08:15:00', 'Yearly');
 
 
-- 1) Subscriptions expiring within the next 10 days (including today)
SELECT * FROM subscriptions
WHERE DATEDIFF(expiry_date, CURDATE()) BETWEEN 0 AND 10;
 
-- 2) Customers who subscribed in the current calendar month
SELECT * FROM subscriptions
WHERE YEAR(start_date) = YEAR(CURDATE())
  AND MONTH(start_date) = MONTH(CURDATE());
 
-- 3) All yearly plans sorted by expiry_date
SELECT * FROM subscriptions
WHERE plan_type = 'Yearly'
ORDER BY expiry_date ASC;
 
-- 4) Subscriptions lasting more than 30 days (Quarterly/Yearly)
-- Method A: by plan type
SELECT * FROM subscriptions
WHERE plan_type IN ('Quarterly', 'Yearly');
 
-- Method B (strict duration): expiry_date > start_date + 30 days
SELECT * FROM subscriptions
WHERE expiry_date > DATE_ADD(start_date, INTERVAL 30 DAY);
 
-- 5) Data quality check: expiry_date earlier than start_date
SELECT * FROM subscriptions
WHERE expiry_date < start_date;
 