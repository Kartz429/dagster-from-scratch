# Day 26 - Dagster Jobs

## 🎯 Goal

Learn:

- What is a Job?
- Why Jobs are used
- How to execute multiple assets together

---

## What is a Job?

A Job is a collection of assets executed together.

Example:

raw_students
↓
clean_students
↓
student_report

can be grouped into:

student_pipeline_job

---

## Benefits

- Easier execution
- Better organization
- Production-ready workflows

---

## Asset Flow

students.csv
↓
raw_students
↓
clean_students
↓
student_report

---

## Job

student_pipeline_job

Runs the complete workflow.

---

## What I Learned

- Dagster Jobs
- Asset Execution
- Workflow Management
- Definitions