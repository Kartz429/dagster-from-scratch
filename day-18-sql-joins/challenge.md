# Day 18 Challenges

Try to write these queries yourself using `main.sql` as reference.
Hints are given if you get stuck — try without looking first!

## Beginner

### Challenge 1: List Every Enrolled Student and Their Course
Show only students who are actually enrolled in a course (no NULLs).

Expected output:
```
student_name   course_name
Aarav          Python
Aarav          SQL
Diya           SQL
```
<details>
<summary>💡 Hint</summary>

Use `INNER JOIN` — it only keeps rows that match on both sides.
</details>

### Challenge 2: Show All Students, Enrolled or Not
Show every student's name and their course. If they have no course, show
NULL instead of skipping them.

Expected output includes Kabir and Meera with `NULL` as their course.
<details>
<summary>💡 Hint</summary>

Use `LEFT JOIN` with `students` as the left (first) table.
</details>

## Intermediate

### Challenge 3: Find Students With No Enrollment
List only the names of students who haven't joined any course yet.

Expected output:
```
Kabir
Meera
```
<details>
<summary>💡 Hint</summary>

Use `LEFT JOIN` then filter with `WHERE e.enrollment_id IS NULL`.
</details>

### Challenge 4: Count Courses Per Student
Show each student's name and how many courses they're enrolled in
(including students with 0 courses).

Expected output:
```
Aarav   2
Diya    1
Kabir   0
Meera   0
```
<details>
<summary>💡 Hint</summary>

Use `LEFT JOIN` + `COUNT(e.enrollment_id)` + `GROUP BY s.student_name`.
Remember: `COUNT(*)` would wrongly count 1 even for students with no match —
use `COUNT(e.enrollment_id)` instead, since NULL values aren't counted.
</details>

## Bonus ⭐

### Challenge 5: Find "Orphan" Enrollments
Find enrollments that point to a student_id that doesn't actually exist in
the `students` table (like our "Dagster" row).

Expected output:
```
Dagster
```
<details>
<summary>💡 Hint</summary>

Use `RIGHT JOIN` (or `LEFT JOIN` with the tables swapped), then filter
`WHERE s.student_id IS NULL`.
</details>

### Challenge 6: Study Buddy Pairs
List every possible pair of two different students, without repeating a
pair in both directions (Aarav-Diya should NOT also appear as Diya-Aarav).

<details>
<summary>💡 Hint</summary>

This is a SELF JOIN. Join `students` to itself and use
`a.student_id < b.student_id` in the ON condition.
</details>
