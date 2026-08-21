# Day 27 - Dagster Resources

## 🎯 Goal

Learn:

- What is a Resource?
- Why Resources are used
- Reading external data using Resources

---

## What is a Resource?

A Resource manages external dependencies.

Examples:

- CSV Files
- Databases
- APIs
- Cloud Storage

---

## Architecture

students.csv
↓
StudentFileResource
↓
raw_students
↓
student_report

---

## Benefits

- Reusable Code
- Cleaner Assets
- Better Organization
- Production Ready

---

## What I Learned

- Dagster Resources
- External Dependencies
- Resource Injection
- Context Usage