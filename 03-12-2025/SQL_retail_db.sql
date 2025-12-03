CREATE DATABASE retail_db;
USE retail_db;

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
email VARCHAR(80),
city VARCHAR(50)
);

CREATE TABLE orders (
order_id INT PRIMARY KEY,
order_date DATE,
customer_id INT NULL,
total_amount DECIMAL(10,2),
product_id INT NULL
);

CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);

INSERT INTO customers VALUES
(1, 'Aisha Khan', 'aisha@xyz.com', 'Mumbai'),
(2, 'Rahul Sharma', 'rahul@xyz.com', 'Delhi'),
(3, 'John Daniel', 'john@xyz.com', 'Bangalore'),
(4, 'Meera Iyer', 'meera@xyz.com', 'Chennai'),
(5, 'Sanjay Patel', 'sanjay@xyz.com', 'Hyderabad');

INSERT INTO products VALUES
(101, 'Laptop HP 15', 'Electronics', 52000),
(102, 'Samsung Phone A54', 'Electronics', 28000),
(103, 'Jeans Blue Fit', 'Fashion', 1500),
(104, 'T-Shirt Classic', 'Fashion', 700),
(105, 'Wireless Mouse', 'Accessories', 900),
(106, 'Rice 5KG Bag', 'Groceries', 320),
(107, 'Olive Oil 1L', 'Groceries', 540),
(108, 'Printer Canon G2012', 'Electronics', 12500);

INSERT INTO orders VALUES
(1001, '2024-01-05', 1, 52000, 101),
(1002, '2024-01-06', 2, 28000, 102),
(1003, '2024-01-07', 3, 1500, 103),
(1004, '2024-01-07', 1, 700, 104),
(1005, '2024-01-08', 2, 900, 105),
(1006, '2024-01-08', NULL, 320, 106), -- customer unknown
(1007, '2024-01-09', 1, 540, NULL), -- product unknown
(1008, '2024-01-10', 3, 12500, 108),
(1009, '2024-01-10', 4, 320, 106),
(1010, '2024-01-11', NULL, 700, 104), -- customer null
(1011, '2024-01-12', 2, 540, 107); -- product exists but never order

#question1
SELECT o.order_id,o.order_date,o.total_amount,c.customer_name,c.email
FROM orders o
LEFT JOIN customers AS c ON o.customer_id = c.customer_id
ORDER BY o.order_id;

#question 2
SELECT DISTINCT p.product_id,p.product_name,p.category,p.price
FROM orders o
INNER JOIN products AS p ON o.product_id = p.product_id;

#question3
SELECT o.order_id,o.order_date,o.total_amount,c.customer_name,p.product_name
FROM orders AS o
LEFT JOIN customers AS c ON o.customer_id = c.customer_id
LEFT JOIN products AS p ON o.product_id = p.product_id
ORDER BY o.order_id;

#question4
SELECT c.customer_name,o.order_id,o.order_date,o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
ORDER BY c.customer_name, o.order_id;

#question5

SELECT DISTINCT p.product_id,p.product_name,p.category
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
WHERE p.category = 'Electronics';

#question6

SELECT DISTINCT c.customer_id,c.customer_name
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
INNER JOIN customers AS c ON o.customer_id = c.customer_id
WHERE p.category = 'Fashion';


#question7

SELECT o.order_id,o.order_date,o.total_amount,c.customer_name,c.email,p.product_name,p.category,p.price
FROM orders o
INNER JOIN customers AS c ON o.customer_id = c.customer_id
INNER JOIN products AS p ON o.product_id = p.product_id
WHERE o.total_amount > 1000
ORDER BY o.total_amount DESC, o.order_id;

#question8

SELECT DISTINCT c.customer_id,c.customer_name,c.email,c.city
FROM customers c
INNER JOIN orders o ON o.customer_id = c.customer_id
WHERE c.city = 'Mumbai';

#question9

SELECT c.customer_id,c.customer_name,COUNT(*) AS order_count
FROM customers c
INNER JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY order_count DESC, c.customer_id;

#question10

SELECT c.customer_id,c.customer_name,
COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM customers AS c
LEFT JOIN orders AS o
ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name;


#question11
SELECT o.order_id,o.order_date,o.total_amount,c.customer_name,c.email
FROM orders o
LEFT JOIN customers c ON o.customer_id=c.customer_id
ORDER BY o.order_id;


#question12
SELECT o.order_id,c.customer_id
FROM orders o
LEFT JOIN customers c on o.customer_id=c.customer_id
WHERE c.customer_id IS NULL
ORDER BY o.order_id;

#question13
SELECT o.order_id,c.city,c.customer_name
FROM orders o
LEFT JOIN customers c ON o.customer_id=c.customer_id;

#question14

SELECT c.customer_name,COUNT(o.order_id) AS order_count
FROM customers AS c
LEFT JOIN orders AS o
ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY order_count DESC, c.customer_name;

#question15
SELECT c.customer_id,c.customer_name
FROM customers c
LEFT JOIN orders o 
ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;

#question16

SELECT o.order_id,o.order_date,o.total_amount,
    CASE 
        WHEN c.customer_name IS NULL THEN 'Guest Checkout'
        ELSE c.customer_name
    END AS customer_name
FROM orders AS o
LEFT JOIN customers AS c ON o.customer_id = c.customer_id
ORDER BY o.order_id;

#question17

SELECT o.order_id
FROM orders o
LEFT JOIN products p ON o.product_id=p.product_id
WHERE p.product_id IS NULL
ORDER BY o.order_id;

#question18

SELECT o.order_id,o.order_date,o.total_amount,c.customer_name,c.city
FROM orders AS o
LEFT JOIN customers AS c ON o.customer_id = c.customer_id
WHERE c.city = 'Delhi' OR c.customer_id IS NULL
ORDER BY o.order_id;

#question19

SELECT COUNT(o.order_id) AS total_orders
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id;


#question20

SELECT 
    ROUND(
        (SUM(CASE WHEN o.customer_id IS NULL THEN 1 ELSE 0 END) * 100.0) / COUNT(o.order_id), 2
    ) AS missing_customer_percentage
FROM orders AS o
LEFT JOIN customers AS c ON o.customer_id = c.customer_id;

#question 21

SELECT p.product_id,p.product_name,p.category,p.price,o.order_id,o.order_date,o.total_amount
FROM orders AS o
RIGHT JOIN products AS p
ON o.product_id = p.product_id
ORDER BY p.product_id, o.order_id;



#question22

SELECT p.product_id,p.product_name,p.category,p.price
FROM orders AS o
RIGHT JOIN products AS p
ON o.product_id = p.product_id
WHERE o.order_id IS NULL
ORDER BY p.product_id;

#question23

SELECT p.product_name,COUNT(o.order_id) AS times_ordered
FROM orders AS o
RIGHT JOIN products AS p
ON o.product_id = p.product_id
WHERE p.category = 'Electronics'
GROUP BY p.product_name;

#qestion 24

SELECT 
    p.product_name,
    MIN(o.order_date) AS first_order_date
FROM orders AS o
RIGHT JOIN products AS p
    ON o.product_id = p.product_id
WHERE p.category = 'Groceries'
GROUP BY p.product_name
ORDER BY p.product_name;

#question 25

SELECT 
    p.product_name,
    COALESCE(SUM(o.total_amount), 0) AS total_sales
FROM orders AS o
RIGHT JOIN products AS p
    ON o.product_id = p.product_id
GROUP BY p.product_name;

#question26

SELECT 
    p.category,
    COUNT(DISTINCT o.product_id) AS ordered_products_count
FROM orders AS o
RIGHT JOIN products AS p
    ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY ordered_products_count DESC;

#question27

SELECT DISTINCT
    p.product_id,
    p.product_name,
    p.category
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
RIGHT JOIN products AS p
    ON o.product_id = p.product_id
WHERE c.city = 'Bangalore';

#question28

SELECT 
    p.product_id,
       p.product_name,
    p.category
FROM orders AS o
RIGHT JOIN products AS p
    ON o.product_id = p.product_id;


#question29

SELECT 
    p.product_name,
    COUNT(o.order_id) AS order_count
FROM orders AS o
RIGHT JOIN products AS p
    ON o.product_id = p.product_id
GROUP BY p.product_name;

#question30

SELECT DISTINCT
    p.product_id,
    p.product_name,
    p.category
FROM orders AS o
RIGHT JOIN products AS p
    ON o.product_id = p.product_id
WHERE o.customer_id IS NULL AND o.order_id IS NOT NULL;
















