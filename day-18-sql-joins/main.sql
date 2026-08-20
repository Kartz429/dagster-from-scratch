-- ========================================
-- 🔗 DAY 18 - SQL JOINS
-- ========================================
-- This file teaches you how to combine data across TWO tables:
-- INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN, CROSS JOIN, SELF JOIN
-- Run each section one at a time and compare your output to the comments.


-- ========================================
-- STEP 1: Create the tables
-- ========================================

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT
);

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT
);


-- ========================================
-- STEP 2: Insert sample data
-- ========================================
-- Notice: Kabir and Meera have NO enrollments.
-- Notice: the "Dagster" enrollment belongs to student_id 5, who doesn't exist.
-- This lets us see how each join type handles missing/unmatched data.

INSERT INTO students (student_id, student_name) VALUES
(1, 'Aarav'),
(2, 'Diya'),
(3, 'Kabir'),
(4, 'Meera');

INSERT INTO enrollments (enrollment_id, student_id, course_name) VALUES
(1, 1, 'Python'),
(2, 1, 'SQL'),
(3, 2, 'SQL'),
(4, 5, 'Dagster');


-- ========================================
-- STEP 3: INNER JOIN — only matching rows
-- ========================================
-- Shows only students who HAVE an enrollment.
-- Kabir, Meera, and the orphan "Dagster" row are excluded.

SELECT s.student_name, e.course_name
FROM students AS s
INNER JOIN enrollments AS e ON s.student_id = e.student_id;

-- Expected:
-- Aarav | Python
-- Aarav | SQL
-- Diya  | SQL


-- ========================================
-- STEP 4: LEFT JOIN — keep everything from students
-- ========================================
-- Shows ALL students, even Kabir and Meera who have no enrollment.
-- Their course_name will show as NULL.

SELECT s.student_name, e.course_name
FROM students AS s
LEFT JOIN enrollments AS e ON s.student_id = e.student_id;

-- Expected:
-- Aarav | Python
-- Aarav | SQL
-- Diya  | SQL
-- Kabir | NULL
-- Meera | NULL


-- ========================================
-- STEP 5: RIGHT JOIN — keep everything from enrollments
-- ========================================
-- Shows ALL enrollments, even the "Dagster" one whose student doesn't exist.
-- That row's student_name will show as NULL.

SELECT s.student_name, e.course_name
FROM students AS s
RIGHT JOIN enrollments AS e ON s.student_id = e.student_id;

-- Expected:
-- Aarav | Python
-- Aarav | SQL
-- Diya  | SQL
-- NULL  | Dagster


-- ========================================
-- STEP 6: FULL OUTER JOIN — keep everything from both tables
-- ========================================
-- Combines LEFT and RIGHT JOIN. Nothing is left out from either table.

SELECT s.student_name, e.course_name
FROM students AS s
FULL OUTER JOIN enrollments AS e ON s.student_id = e.student_id;

-- Expected:
-- Aarav | Python
-- Aarav | SQL
-- Diya  | SQL
-- Kabir | NULL
-- Meera | NULL
-- NULL  | Dagster


-- ========================================
-- STEP 7: CROSS JOIN — every combination
-- ========================================
-- Matches EVERY student with EVERY enrollment. No ON condition needed.
-- 4 students x 4 enrollments = 16 rows. Use with caution on big tables!

SELECT s.student_name, e.course_name
FROM students AS s
CROSS JOIN enrollments AS e;


-- ========================================
-- STEP 8: SELF JOIN — join a table to itself
-- ========================================
-- Pairs every student with every OTHER student (like possible study buddies).
-- The "<" avoids matching a student with themselves and avoids duplicate pairs.

SELECT a.student_name AS student_a, b.student_name AS student_b
FROM students AS a
JOIN students AS b ON a.student_id < b.student_id;


-- ========================================
-- STEP 9: Find students with NO enrollment
-- ========================================
-- A very common real-world question: "who hasn't signed up for anything?"
-- We use LEFT JOIN + check WHERE the match is missing (IS NULL).

SELECT s.student_name
FROM students AS s
LEFT JOIN enrollments AS e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;

-- Expected:
-- Kabir
-- Meera


-- ========================================
-- STEP 10: JOIN + GROUP BY (using Day 17 skills)
-- ========================================
-- "How many courses has each student enrolled in?"
-- LEFT JOIN keeps every student, COUNT() counts their courses (0 if none).

SELECT s.student_name, COUNT(e.enrollment_id) AS total_courses
FROM students AS s
LEFT JOIN enrollments AS e ON s.student_id = e.student_id
GROUP BY s.student_name;

-- Expected:
-- Aarav | 2
-- Diya  | 1
-- Kabir | 0
-- Meera | 0
