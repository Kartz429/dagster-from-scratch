# Day 30 Test Cases

## Test Case 1

Cron:

0 6 * * *

Expected:

Runs Daily At 6 AM

✅ Pass

---

## Test Case 2

Cron:

0 0 * * *

Expected:

Runs Daily At Midnight

✅ Pass

---

## Test Case 3

Cron:

0 * * * *

Expected:

Runs Every Hour

✅ Pass

---

## Edge Case

Schedule Disabled

Expected:

Pipeline Does Not Run

✅ Pass