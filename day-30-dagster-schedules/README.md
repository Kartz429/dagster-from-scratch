# Day 30 - Dagster Schedules

## 🎯 Goal

Learn:

- What are Schedules?
- Cron Expressions
- Automatic Pipeline Execution

---

## What is a Schedule?

A Schedule automatically runs a Job.

Example:

Every Day at 6 AM

↓

Generate Report

---

## Example

```python
ScheduleDefinition(
    job_name="daily_report_job",
    cron_schedule="0 6 * * *"
)
```

---

## Benefits

- Automation
- No Manual Work
- Reliable Execution

---

## What I Learned

- Dagster Schedules
- Cron Expressions
- Automated Data Pipelines