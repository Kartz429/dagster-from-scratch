# Day 18 - SQL Joins

## Goal
Learn how to combine data that is spread across **two tables** into one result.
Until now we only worked with one table at a time. Real databases almost
always split information into multiple related tables — Joins are how you
bring them back together.

## Our Two Tables
**students** — one row per student
```
student_id | student_name
1          | Aarav
2          | Diya
3          | Kabir
4          | Meera
```

**enrollments** — one row per course a student has signed up for
```
enrollment_id | student_id | course_name
1             | 1          | Python
2             | 1          | SQL
3             | 2          | SQL
4             | 5          | Dagster   <- student_id 5 does not exist in students!
```

Notice two tricky things on purpose:
* **Kabir** and **Meera** exist in `students` but have **no rows** in `enrollments` (they haven't joined any course).
* The `Dagster` enrollment points to `student_id = 5`, which **doesn't exist** in `students` (a leftover/orphan record).

This is exactly the kind of messy real-world data joins help you deal with.

## Concepts Used (Explained Simply)

### 1. INNER JOIN — "Only show matches"
Returns rows **only when both tables have matching data**.
```sql
SELECT s.student_name, e.course_name
FROM students AS s
INNER JOIN enrollments AS e ON s.student_id = e.student_id;
```
Kabir, Meera, and the orphan "Dagster" row are all **left out**, because
there's no match on both sides.

### 2. LEFT JOIN — "Keep everything from the left table"
Returns **all rows from the first (left) table**, even if there's no match
in the second table. Missing values become `NULL`.
```sql
SELECT s.student_name, e.course_name
FROM students AS s
LEFT JOIN enrollments AS e ON s.student_id = e.student_id;
```
Now Kabir and Meera **do** appear, with `course_name = NULL`, because they
have no enrollment — but they're still students, so LEFT JOIN keeps them.

### 3. RIGHT JOIN — "Keep everything from the right table"
The opposite of LEFT JOIN — keeps all rows from the second (right) table.
```sql
SELECT s.student_name, e.course_name
FROM students AS s
RIGHT JOIN enrollments AS e ON s.student_id = e.student_id;
```
Now the "Dagster" enrollment appears with `student_name = NULL`, because
that enrollment's student doesn't actually exist.

### 4. FULL OUTER JOIN — "Keep everything from both sides"
Combines LEFT JOIN and RIGHT JOIN — nothing gets left out from either table.
```sql
SELECT s.student_name, e.course_name
FROM students AS s
FULL OUTER JOIN enrollments AS e ON s.student_id = e.student_id;
```
You get matched rows, Kabir/Meera with NULL courses, AND the orphan
Dagster row with a NULL student — everything, from both tables.

### 5. CROSS JOIN — "Match everything with everything"
Combines **every row** of one table with **every row** of the other. No ON
condition is used. Be careful — this grows fast! (4 students × 4
enrollments = 16 rows here.)
```sql
SELECT s.student_name, e.course_name
FROM students AS s
CROSS JOIN enrollments AS e;
```
Rarely used in real work, but good to know — mostly used to generate
combinations (like "every product in every store").

### 6. SELF JOIN — "Join a table to itself"
Useful when you want to compare rows **within the same table**. Here, we
pair up every student with every other student (like generating a list of
possible study partners).
```sql
SELECT a.student_name AS student_a, b.student_name AS student_b
FROM students AS a
JOIN students AS b ON a.student_id < b.student_id;
```
The `<` avoids pairing a student with themselves and avoids duplicate
pairs (Aarav-Diya and Diya-Aarav counted once).

## Table Aliases (`AS s`, `AS e`)
Instead of typing `students.student_name` every time, we give the table a
short nickname:
```sql
FROM students AS s
```
Now we can just write `s.student_name`. This is optional but makes joins
much easier to read, especially with two tables in one query.

## Finding Unmatched Rows
A very common real task: "show me students who have NOT enrolled in
anything." Combine LEFT JOIN with `IS NULL`:
```sql
SELECT s.student_name
FROM students AS s
LEFT JOIN enrollments AS e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;
```
This works because unmatched students get `NULL` in the enrollment
columns — so filtering for `NULL` finds exactly the ones with no match.

## Combining Joins with GROUP BY (from Day 17)
```sql
SELECT s.student_name, COUNT(e.enrollment_id) AS total_courses
FROM students AS s
LEFT JOIN enrollments AS e ON s.student_id = e.student_id
GROUP BY s.student_name;
```
This answers "how many courses has each student enrolled in?" — and
correctly shows `0` for Kabir and Meera instead of leaving them out.

## Cheat Sheet
| Join Type   | Keeps                                    |
|-------------|-------------------------------------------|
| INNER JOIN  | Only matching rows from both tables        |
| LEFT JOIN   | All rows from the left table + matches     |
| RIGHT JOIN  | All rows from the right table + matches    |
| FULL OUTER  | All rows from both tables                  |
| CROSS JOIN  | Every combination of rows (no match needed)|
| SELF JOIN   | A table joined with itself                 |

## How to Run This
1. Open any SQLite tool (e.g. sqliteonline.com or DB Browser for SQLite)
2. Copy the contents of `main.sql`
3. Run it section by section and compare your output with the comments

## What I Learned
   * How to combine two related tables into one meaningful result
   * The difference between INNER, LEFT, RIGHT, and FULL OUTER JOIN
   * How to find rows in one table that have no match in another
   * How to compare rows within the same table using a SELF JOIN
   * How joins and GROUP BY work together to summarize related data
