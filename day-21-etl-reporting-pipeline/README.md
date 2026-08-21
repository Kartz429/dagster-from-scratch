# Day 21 - ETL Reporting Pipeline 📊

## 🎯 Goal

Learn how to build an end-to-end ETL pipeline that:

1. Creates raw data
2. Extracts data
3. Transforms data
4. Loads clean data
5. Generates analytics
6. Creates a business report

---

## 🧠 Simple Explanation

Imagine a school principal wants a daily report.

Raw data:

```text
Kartik - 95
Rahul - 88
Priya - 91
```

The principal doesn't want raw data.

The principal wants:

```text
Total Students
Average Marks
Highest Marks
Top Student
```

Our ETL pipeline converts raw data into useful information.

---

## 📦 What is ETL?

### Extract

Read the data.

Example:

```text
students.csv
```

---

### Transform

Clean and standardize the data.

Before:

```text
kartik,mumbai,95
```

After:

```text
Kartik,Mumbai,95
```

---

### Load

Store cleaned data.

Example:

```text
clean_students.csv
```

---

## 🔄 Project Workflow

```text
create_students_csv.py
          ↓
      students.csv
          ↓
      ETL Pipeline
          ↓
  clean_students.csv
          ↓
      Analytics
          ↓
       report.txt
```

---

## 📂 Project Files

### create_students_csv.py

Creates raw student data.

---

### students.csv

Stores raw student records.

---

### etl_pipeline.py

Performs:

- Extract
- Transform
- Load

operations.

---

### clean_students.csv

Stores cleaned records.

---

### analytics.py

Calculates:

- Total Students
- Average Marks
- Highest Marks
- Lowest Marks
- Top Student

---

### report.txt

Final business report.

---

## 📊 Example Report

```text
STUDENT REPORT
==============================

Total Students : 5
Average Marks : 87.40
Highest Marks : 95
Lowest Marks : 78
Top Student : Kartik
```

---

## 🚀 Why This Matters

This is exactly how Data Engineering works.

Today:

```text
CSV
 ↓
ETL
 ↓
Analytics
 ↓
Report
```

Tomorrow:

```text
Database
 ↓
ETL Pipeline
 ↓
Data Warehouse
 ↓
Dashboard
```

And later in Dagster:

```python
@asset
def clean_students():
    ...
```

```python
@asset
def student_report():
    ...
```

---

## ✅ What I Learned

- CSV Processing
- ETL Fundamentals
- Data Cleaning
- Analytics Generation
- Report Creation
- Business Metrics

---

## 🏗 Skills Used

- Python
- CSV Module
- File Handling
- Lists
- Dictionaries
- ETL Concepts
- Analytics

---

## ▶️ How To Run

Step 1:

```bash
python create_students_csv.py
```

Step 2:

```bash
python etl_pipeline.py
```

Step 3:

```bash
python analytics.py
```

---

## 🎉 Outcome

By the end of this project I can:

✅ Create raw datasets

✅ Transform and clean data

✅ Generate analytics

✅ Produce