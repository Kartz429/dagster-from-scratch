# Day 17 Test Cases

Run each query in `main.sql` against the sample data and check if your
result matches the expected output below.

## Test Case 1: Total Products
```
Query: SELECT COUNT(*) FROM sales;
Expected: 7
Why: There are exactly 7 rows (products) in the table.
```
✅ Pass

## Test Case 2: Total Sales Value
```
Query: SELECT SUM(price * quantity) FROM sales;
Expected: 219500
Why: (50000*2)+(20000*5)+(1500*10)+(1200*8)+(50*30)+(40*100)+(10*200) = 219500
```
✅ Pass

## Test Case 3: Average Price
```
Query: SELECT AVG(price) FROM sales;
Expected: 10400
Why: (50000+20000+1500+1200+50+40+10) / 7 = 10400
```
✅ Pass

## Test Case 4: Category Grouping
```
Query: SELECT category, COUNT(*) FROM sales GROUP BY category;
Expected:
  Electronics  → 3
  Grocery      → 2
  Stationery   → 2
Why: 3 products belong to Electronics, 2 to Grocery, 2 to Stationery.
```
✅ Pass

## Edge Case: HAVING with No Matching Groups
```
Query: SELECT category, SUM(price * quantity) FROM sales
       GROUP BY category HAVING SUM(price * quantity) > 1000000;
Expected: No rows returned (empty result)
Why: No category's total sales value goes above 1,000,000.
```
✅ Pass
