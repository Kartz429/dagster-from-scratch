# Day 24 - Introduction to Dagster

## 🎯 Goal

Learn:

- What is Dagster?
- Why Data Engineers use Dagster
- What is an Asset?
- Asset Dependencies

---

## What is Dagster?

Dagster is a Data Orchestration Platform.

It helps:

- Run Pipelines
- Manage Dependencies
- Schedule Jobs
- Monitor Data Workflows

---

## What is an Asset?

An asset is a piece of data.

Examples:

- Clean CSV
- Daily Report
- Analytics Table

---

## Example

```python
@asset
def student_count():
    return 5
```

---

## Asset Dependency

```python
student_count
       ↓
      report
```

Dagster automatically manages execution order.

---

## What I Learned

- Dagster Basics
- Assets
- Dependencies
- Data Orchestration