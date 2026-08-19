-- ========================================
-- 📊 DAY 17 - SALES AGGREGATION SYSTEM
-- ========================================
-- This file teaches you SQL Aggregate Functions:
-- COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING
-- Run each section one at a time and look at the result.


-- ========================================
-- STEP 1: Create the table
-- ========================================
-- This table stores products we sold, their category, price, and quantity.

CREATE TABLE sales (
    id INTEGER PRIMARY KEY,     -- unique id for each row
    product_name TEXT,          -- name of the product
    category TEXT,              -- which category it belongs to
    price INTEGER,              -- price of ONE unit
    quantity INTEGER            -- how many units were sold
);


-- ========================================
-- STEP 2: Insert sample data
-- ========================================
-- We add 7 products across 3 categories: Electronics, Grocery, Stationery.

INSERT INTO sales (id, product_name, category, price, quantity) VALUES
(1, 'Laptop',     'Electronics', 50000, 2),
(2, 'Mobile',     'Electronics', 20000, 5),
(3, 'Headphones', 'Electronics', 1500,  10),
(4, 'Rice Bag',   'Grocery',     1200,  8),
(5, 'Milk',       'Grocery',     50,    30),
(6, 'Notebook',   'Stationery',  40,    100),
(7, 'Pen',        'Stationery',  10,    200);


-- ========================================
-- STEP 3: Basic Aggregate Functions
-- ========================================

-- 🔹 COUNT: How many products do we have in total?
-- COUNT(*) simply counts the number of rows.
SELECT COUNT(*) AS total_products
FROM sales;


-- 🔹 SUM: What is the total sales value?
-- price * quantity gives the sales value of EACH row.
-- SUM() then adds all those values together into one number.
SELECT SUM(price * quantity) AS total_sales_value
FROM sales;


-- 🔹 AVG: What is the average price of all products?
-- AVG() adds all prices and divides by the number of rows.
SELECT AVG(price) AS average_price
FROM sales;


-- 🔹 MIN & MAX: What is the cheapest and most expensive product?
SELECT MIN(price) AS cheapest_product,
       MAX(price) AS costliest_product
FROM sales;


-- ========================================
-- STEP 4: Grouping Data with GROUP BY
-- ========================================
-- GROUP BY splits the table into smaller groups (one group per category)
-- BEFORE the aggregate function runs on each group.

-- 🔹 Total sales value PER category
SELECT category,
       SUM(price * quantity) AS total_sales_value
FROM sales
GROUP BY category;

-- 🔹 How many products are in EACH category?
SELECT category,
       COUNT(*) AS product_count
FROM sales
GROUP BY category;


-- ========================================
-- STEP 5: Filtering Groups with HAVING
-- ========================================
-- HAVING works like WHERE, but it filters GROUPS (after aggregation)
-- instead of individual rows.

-- 🔹 Show only categories with total sales value above 50000
SELECT category,
       SUM(price * quantity) AS total_sales_value
FROM sales
GROUP BY category
HAVING SUM(price * quantity) > 50000;

-- Beginner Note:
-- ❌ This will NOT work:
--   SELECT category FROM sales WHERE SUM(price) > 50000 GROUP BY category;
-- ✅ Use HAVING instead of WHERE when filtering on an aggregate function.
