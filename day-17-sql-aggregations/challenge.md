# Day 17 Challenges

Try to write these queries yourself using `main.sql` as reference.
Hints are given if you get stuck — try without looking first!

## Challenge 1: Average Price per Category
Find the average product price, split by category.

Example output:
```
category      average_price
Electronics   23833
Grocery       625
Stationery    25
```
<details>
<summary>💡 Hint</summary>

Use `AVG()` together with `GROUP BY category`.
</details>

## Challenge 2: Category with the Highest Total Sales
Find which single category made the most money.

Example output:
```
category      total_sales_value
Electronics   215500
```
<details>
<summary>💡 Hint</summary>

Use `SUM()`, `GROUP BY`, then `ORDER BY total_sales_value DESC LIMIT 1`.
</details>

## Challenge 3: Categories with More Than 2 Products
Show only categories that contain more than 2 different products.

Example output:
```
category      product_count
Electronics   3
Stationery    2
```
<details>
<summary>💡 Hint</summary>

Use `COUNT(*)`, `GROUP BY category`, then `HAVING COUNT(*) > 2`.
</details>

## Bonus Challenge ⭐
Build a Full Sales Summary Report in ONE set of queries.

Include:
1. Total Products (`COUNT`)
2. Total Sales Value (`SUM`)
3. Average Price (`AVG`)
4. Cheapest Product (`MIN`)
5. Costliest Product (`MAX`)
6. Total Sales Value per Category (`GROUP BY`)

<details>
<summary>💡 Hint</summary>

You can combine the first 5 into one SELECT statement, then write a
separate query with GROUP BY for the category breakdown.
</details>
