# Day 17 - SQL Aggregations

## Goal
Learn how to take a big table of data and turn it into simple, useful summaries.
Example: Instead of looking at 1000 rows of sales, we ask "What is the TOTAL sales?" in one line of SQL.

## What is an Aggregate Function?
An aggregate function takes **many rows** and gives back **one answer**.

Think of it like this:
```
You have 7 products in a table.
COUNT(*) → tells you there are 7 products (one number).
SUM(price) → adds all prices together (one number).
```

## Concepts Used (Explained Simply)

### 1. COUNT()
Counts how many rows there are.
```sql
SELECT COUNT(*) FROM sales;
-- "How many products do I have?"
```

### 2. SUM()
Adds up a column of numbers.
```sql
SELECT SUM(price) FROM sales;
-- "What is the total price of everything?"
```

### 3. AVG()
Finds the average (mean) of a column.
```sql
SELECT AVG(price) FROM sales;
-- "What is the average price?"
```

### 4. MIN() and MAX()
Finds the smallest and largest value.
```sql
SELECT MIN(price), MAX(price) FROM sales;
-- "What is the cheapest and most expensive product?"
```

### 5. GROUP BY
Splits your data into groups BEFORE you aggregate.
```sql
SELECT category, SUM(price) FROM sales GROUP BY category;
-- "Give me the total price, but split it by category"
```
Without GROUP BY, SUM() adds everything together as one big group.
With GROUP BY, SUM() adds each category separately.

### 6. HAVING
Filters groups AFTER they have been aggregated.
```sql
SELECT category, SUM(price) FROM sales
GROUP BY category
HAVING SUM(price) > 50000;
-- "Only show me categories whose total price is above 50000"
```

**Important beginner tip:**
`WHERE` filters rows BEFORE grouping.
`HAVING` filters groups AFTER grouping.
You cannot use `WHERE` to filter on `SUM()`, `AVG()`, etc. — that's what `HAVING` is for.

## Project
Sales Aggregation System

We use one simple table called `sales` and answer real business questions:
   * How many products do we sell?
   * What is our total sales value?
   * What is the average price?
   * Which category earns the most?
   * Which categories sell the most items?

## How to Run This
1. Open any SQLite tool (e.g. sqliteonline.com or DB Browser for SQLite)
2. Copy the contents of `main.sql`
3. Run it step by step (create table → insert data → try each query one at a time)

## What I Learned
   * How to summarize large datasets into simple insights using one line of SQL
   * The difference between `WHERE` (filters rows) and `HAVING` (filters groups)
   * How `GROUP BY` organizes data into buckets before aggregating
   * Writing beginner-friendly, well-commented SQL queries
