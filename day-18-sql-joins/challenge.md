# Day 18 Challenges

These challenges get harder step by step. Do them in order — each one
builds on the skill from the one before it. Use `main.sql` as your
reference if you get stuck.

Reminder of our two tables:
```
students: student_id, student_name
enrollments: enrollment_id, student_id, course_name
```

---

## Challenge 1: Just Fill in the Blank (Easiest)
Below is a working query with one word missing. Just figure out which
join type goes in the blank so that it shows **only** students who
actually have a course.

```sql
SELECT s.student_name, e.course_name
FROM students AS s
______ JOIN enrollments AS e ON s.student_id = e.student_id;
```

Expected output (3 rows only):
```
Aarav | Python
Aarav | SQL
Diya  | SQL
```
<details>
<summary>💡 Hint</summary>

You want ONLY matches, nothing extra. Which join keeps only rows that
exist in both tables? (Check the cheat sheet in README.md)
</details>

---

## Challenge 2: Change One Word to See What Happens
Take your query from Challenge 1 and change just the join type so that
Kabir and Meera also show up (with `NULL` as their course).

Expected output (5 rows):
```
Aarav | Python
Aarav | SQL
Diya  | SQL
Kabir | NULL
Meera | NULL
```
<details>
<summary>💡 Hint</summary>

You now want ALL students, even ones with no match. Which join always
keeps everything from the FIRST (left) table?
</details>

---

## Challenge 3: Write It Yourself — Find Who Hasn't Joined Anything
Using your Challenge 2 query as a base, add ONE more line to filter down
to just the students with no course.

Expected output:
```
Kabir
Meera
```
<details>
<summary>💡 Hint</summary>

Step 1: Start from your Challenge 2 query (LEFT JOIN).
Step 2: Add `WHERE e.enrollment_id IS NULL` at the end.
Step 3: Only SELECT `s.student_name` — you don't need the course column
anymore since it will always be NULL.
</details>

---

## Challenge 4: Count Instead of List
Instead of listing student names, write a query that counts how many
courses EACH student is enrolled in — including students with 0.

Expected output:
```
Aarav | 2
Diya  | 1
Kabir | 0
Meera | 0
```
<details>
<summary>💡 Hint</summary>

Step 1: Start with a LEFT JOIN (like Challenge 2) so nobody gets left out.
Step 2: Replace `e.course_name` in your SELECT with `COUNT(e.enrollment_id)`.
Step 3: Add `GROUP BY s.student_name` at the end so it counts PER student.
</details>

---

## Challenge 5: Spot the Problem Row
One enrollment in our table points to a `student_id` that doesn't exist
in the `students` table. Write a query that finds it.

Expected output:
```
Dagster
```
<details>
<summary>💡 Hint</summary>

Step 1: This time you need to keep everything from `enrollments`
(the RIGHT side), not `students`. Use RIGHT JOIN instead of LEFT JOIN.
Step 2: Add `WHERE s.student_id IS NULL` to find the row with no
matching student.
Step 3: SELECT `e.course_name` to see which course it was.
</details>

---

## Bonus ⭐: Study Buddy Pairs
List every possible pair of two DIFFERENT students, without showing the
same pair twice (e.g. don't show both "Aarav-Diya" AND "Diya-Aarav").

<details>
<summary>💡 Hint</summary>

This one is a SELF JOIN — join the `students` table to itself using two
different aliases, like `a` and `b`:
```sql
FROM students AS a
JOIN students AS b ON a.student_id < b.student_id
```
The `<` (less than) is the trick that stops duplicate pairs and stops a
student from being paired with themselves.
</details>
