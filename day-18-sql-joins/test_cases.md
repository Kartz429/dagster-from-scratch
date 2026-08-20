# Day 18 Test Cases

Run each query in `main.sql` against the sample data and check if your
result matches the expected output below. All results below were run and
verified against a real SQLite database.

## Test Case 1: INNER JOIN
```
Query: SELECT s.student_name, e.course_name
       FROM students AS s
       INNER JOIN enrollments AS e ON s.student_id = e.student_id;
Expected:
  Aarav | Python
  Aarav | SQL
  Diya  | SQL
Why: Only students WITH a matching enrollment are shown. Kabir, Meera,
     and the orphan "Dagster" row are excluded.
```
✅ Pass

## Test Case 2: LEFT JOIN
```
Query: SELECT s.student_name, e.course_name
       FROM students AS s
       LEFT JOIN enrollments AS e ON s.student_id = e.student_id;
Expected:
  Aarav | Python
  Aarav | SQL
  Diya  | SQL
  Kabir | NULL
  Meera | NULL
Why: ALL students are kept, even ones with no enrollment. Missing
     matches become NULL instead of disappearing.
```
✅ Pass

## Test Case 3: RIGHT JOIN
```
Query: SELECT s.student_name, e.course_name
       FROM students AS s
       RIGHT JOIN enrollments AS e ON s.student_id = e.student_id;
Expected:
  Aarav | Python
  Aarav | SQL
  Diya  | SQL
  NULL  | Dagster
Why: ALL enrollments are kept, even the "Dagster" one whose student_id (5)
     doesn't exist in the students table.
```
✅ Pass

## Test Case 4: Students With No Enrollment
```
Query: SELECT s.student_name
       FROM students AS s
       LEFT JOIN enrollments AS e ON s.student_id = e.student_id
       WHERE e.enrollment_id IS NULL;
Expected:
  Kabir
  Meera
Why: These are the only students whose LEFT JOIN produced no match,
     so their enrollment_id came back as NULL.
```
✅ Pass

## Test Case 5: Join + GROUP BY Count
```
Query: SELECT s.student_name, COUNT(e.enrollment_id) AS total_courses
       FROM students AS s
       LEFT JOIN enrollments AS e ON s.student_id = e.student_id
       GROUP BY s.student_name;
Expected:
  Aarav | 2
  Diya  | 1
  Kabir | 0
  Meera | 0
Why: COUNT(e.enrollment_id) only counts actual (non-NULL) enrollment
     rows, so students with no matches correctly show 0, not 1.
```
✅ Pass

## Edge Case: CROSS JOIN Row Count
```
Query: SELECT COUNT(*) FROM students CROSS JOIN enrollments;
Expected: 16
Why: CROSS JOIN pairs every row in students (4) with every row in
     enrollments (4) → 4 x 4 = 16 combinations, no matching required.
```
✅ Pass
