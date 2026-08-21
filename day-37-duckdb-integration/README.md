# Day 37 - DuckDB Integration 🦆

## 🎯 Goal

Learn:

- DuckDB
- Analytical Databases
- Dagster + DuckDB Integration
- Data Warehousing
- SQL Analytics

---

## What is DuckDB?

DuckDB is a lightweight analytical database.

Think:

```text
SQLite → Application Database

DuckDB → Analytics Database
```

DuckDB is designed for analytical workloads and fast queries.

---

## Why DuckDB?

Data Engineers commonly use:

- DuckDB
- Snowflake
- BigQuery
- Redshift
- Databricks

DuckDB is perfect for learning modern analytics engineering concepts locally.

---

## Pipeline Architecture

```text
students.csv
      ↓
raw_students
      ↓
load_to_duckdb
      ↓
student_warehouse.duckdb
      ↓
analytics_report
```

---

## Project Features

✅ Read CSV Data

✅ Load Data Into DuckDB

✅ Create Warehouse Table

✅ Execute SQL Analytics

✅ Generate Business Metrics

✅ Dagster Integration

---

## Assets

### raw_students

Reads data from students.csv.

---

### load_to_duckdb

Creates table and loads data into DuckDB.

---

### analytics_report

Calculates:

- Total Students
- Average Marks
- Highest Marks

---

## Example Analytics

```python
{
    "total_students": 4,
    "average_marks": 88.0,
    "highest_marks": 95
}
```

---

## What I Learned

- DuckDB Basics
- Data Warehousing
- SQL Analytics
- Dagster Assets
- Warehouse Loading
- Analytics Pipelines

---

## How To Run

Install DuckDB:

```bash
pip install duckdb
```

Run Dagster:

```bash
dagster dev
```

Open:

```text
http://localhost:3000
```

Materialize:

```text
raw_students
↓
load_to_duckdb
↓
analytics_report
```

---

## Outcome

By the end of this project I can:

✅ Load CSV data into a warehouse

✅ Run SQL analytics

✅ Integrate DuckDB with Dagster

✅ Build warehouse-powered data pipelines