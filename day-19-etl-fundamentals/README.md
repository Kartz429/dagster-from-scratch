# Day 19 - ETL Fundamentals

## 🎯 Goal

Learn how Data Engineers move data from one place to another.

ETL stands for:

```text
Extract → Transform → Load
```

---

## What is ETL?

### Extract

Get data from a source.

Examples:

- CSV
- Excel
- API
- Database

---

### Transform

Clean or modify data.

Examples:

- Fix names
- Remove duplicates
- Standardize formats

---

### Load

Store cleaned data.

Examples:

- CSV
- Database
- Data Warehouse

---

## Project Flow

```text
create_students_csv.py
          ↓
      students.csv
          ↓
      etl_pipeline.py
          ↓
  clean_students.csv
          ↓
      analytics.py
          ↓
      Report
```

---

## Files

### create_students_csv.py

Creates raw student data.

### etl_pipeline.py

Performs ETL operations.

### analytics.py

Generates insights and statistics.

---

## What I Learned

- ETL Basics
- CSV Processing
- Data Cleaning
- Analytics
- Data Engineering Workflow

---

## Real World Usage

Used in:

- Data Engineering
- ETL Pipelines
- Data Warehouses
- Analytics
- Dagster Pipelines