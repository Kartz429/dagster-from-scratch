# Day 39 - Production Data Project

## Goal

Build a production-style Dagster pipeline.

## Architecture

students.csv
↓
raw_students
↓
clean_students
↓
marks_validation
↓
warehouse_students
↓
analytics_dashboard
↓
report

## Concepts Used

- Assets
- Asset Checks
- Jobs
- Schedules
- Sensors
- DuckDB

## Output

dashboard_report.txt

## What I Learned

- Production ETL Design
- Data Validation
- Data Warehouse Loading
- Dashboard Analytics
- Automation